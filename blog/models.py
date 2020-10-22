from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Blog(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True)

    def __str__(self):
        return f"{self.author.username}'s blog"


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='parent_blog')
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    readers = models.ManyToManyField(User, related_name='post_readers', blank=True)

    def get_absolute_url(self):
        return reverse("blog:post", args=(self.id,))

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
