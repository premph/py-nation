# Generated by Django 2.0.6 on 2018-06-21 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallthings', '0009_auto_20180621_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='newpost',
            name='thumb',
        ),
    ]
