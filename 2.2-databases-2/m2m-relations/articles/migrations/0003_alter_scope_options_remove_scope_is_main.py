# Generated by Django 4.0.4 on 2022-04-14 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={},
        ),
        migrations.RemoveField(
            model_name='scope',
            name='is_main',
        ),
    ]
