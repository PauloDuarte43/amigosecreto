from django.contrib import admin
from django.http import HttpResponse
from .models import Friend
from urllib.parse import urlencode

def generate_login_urls(modeladmin, request, queryset):
    """
    Gera URLs de login automático para os usuários selecionados
    """
    base_url = request.build_absolute_uri('/?')
    urls = []
    
    for friend in queryset:
        params = urlencode({'username': friend.username, 'password': friend.password})
        url = f"{base_url}{params}"
        urls.append(url)
    
    response_content = "\n".join(urls)
    
    # Retorna como texto para download
    response = HttpResponse(response_content, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="login_urls.txt"'
    return response

generate_login_urls.short_description = "Gerar URLs de login automático"

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'password', 'secret_friend')
    actions = [generate_login_urls]
