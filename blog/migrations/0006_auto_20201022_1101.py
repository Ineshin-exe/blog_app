# Generated by Django 3.1.2 on 2020-10-22 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20201022_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptions',
            name='blogs',
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='blogs',
            field=models.ManyToManyField(related_name='subscribed_blogs', to='blog.Blog'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
