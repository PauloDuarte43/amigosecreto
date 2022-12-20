import random
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import Friend


def index(request):
    msg = ''
    logged_friend = None
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST['username']
            try:
                friend = Friend.objects.get(
                        Q(username=username)|Q(name=username),
                        password=request.POST['password'])
            except:
                friend = None

            if friend:
                logged_friend = friend
                if request.POST.get('gift'):
                    friend.desired_gift = request.POST['gift']

                if not friend.secret_friend:
                    _fns = Friend.objects.filter(
                        secret_friend__isnull=False
                    )

                    if _fns:
                        _rnd_friend = Friend.objects.exclude(id=friend.id, id__in=[i.secret_friend.id for i in _fns])
                    else:
                        _rnd_friend = Friend.objects.exclude(id=friend.id)

                    friend.secret_friend = random.choice(_rnd_friend)

                friend.save()

            else:
                msg = 'Usuário ou senha inválidos!'
        else:
            msg = 'Usuário ou senha inválidos!'

    friend_no_secret = Friend.objects.exclude(
        secret_friend__isnull=False
    ).order_by('username')

    friend_desired_gift = Friend.objects.filter(
        desired_gift__isnull=False
    ).order_by('username')

    context = {
        'logged_friend': logged_friend,
        'message': msg,
        'friend_no_secret': friend_no_secret,
        'friend_desired_gift': friend_desired_gift
    }

    return render(request, 'home/index.html', context)
