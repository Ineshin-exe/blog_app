from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.username}'s blog"


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title
