# Generated by Django 4.0.4 on 2022-04-28 08:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0002_advertisement_who_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='who_liked',
            field=models.ManyToManyField(blank=True, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
