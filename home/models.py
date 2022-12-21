import random
import string

from django.db import models


def rand_str(): 
    return ''.join(random.choice(string.ascii_lowercase) for i in range(4))


class Friend(models.Model):
    username = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=20, null=False, default=rand_str)
    desired_gift = models.CharField(max_length=200, null=True, blank=True)
    secret_friend = models.ForeignKey('Friend', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.username} - {self.password} - {self.secret_friend is not None}'

