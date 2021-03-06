# Generated by Django 3.1.2 on 2020-10-22 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20201022_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='subscribers',
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_blogs', to='blog.blog')),
                ('subscriber', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
