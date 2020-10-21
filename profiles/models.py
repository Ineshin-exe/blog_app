from django.contrib.auth.models import User
from django.db import models

from blog.models import Blog, Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Blog, null=True, blank=True)
    read = models.ManyToManyField(Post, null=True, blank=True)

    def __str__(self):
        return self.user.username
