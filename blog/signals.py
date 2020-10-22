from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Blog, Post


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(owner=instance)


@receiver(post_save, sender=Post)
def send_notification(sender, instance, created, **kwargs):
    if created:
        subscribers = instance.blog.subscribers.all()
        for subscriber in subscribers:
            send_mail(
                'New post!',
                f'http://127.0.0.1:8000{Post.get_absolute_url(instance)}',
                'nikesh.white@gmail.com',
                [subscriber.email],
                fail_silently=False
            )
