# Generated by Django 2.0.6 on 2018-06-21 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallthings', '0011_auto_20180621_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created',
        ),
    ]
