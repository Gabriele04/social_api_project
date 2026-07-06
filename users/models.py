from django.db import models
from django.contrib.auth.models import AbstractUser

class SocialUser(AbstractUser):
    #ha già username password email da Abstract User
    ROLE = (('user', 'Social User'), ('moderator', 'Moderator'),)

    role = models.CharField(max_length=10, choices=ROLE, default='user')
    bio = models.TextField(max_length=100, blank=True)
    occupation = models.TextField(max_length=30, blank=True)
    following = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.username