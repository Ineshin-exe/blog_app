from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from blog_app.settings import SEND_EMAIL_SITE_URL, EMAIL_HOST_USER

from blog.models import Blog, Post


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(author=instance)


# Set SEND_EMAIL_SITE_URL in .env file
@receiver(post_save, sender=Post)
def send_notification(sender, instance, created, **kwargs):
    if created:
        subscribers = instance.blog.subscribers.all()
        for subscriber in subscribers:
            send_mail(
                f'New post by {instance.blog.author}!',
                f'http://{SEND_EMAIL_SITE_URL}{Post.get_absolute_url(instance)}',
                f'{EMAIL_HOST_USER}',
                [subscriber.email],
                fail_silently=False
            )
