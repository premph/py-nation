# Generated by Django 2.0.6 on 2018-06-24 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallthings', '0016_auto_20180624_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
    ]
