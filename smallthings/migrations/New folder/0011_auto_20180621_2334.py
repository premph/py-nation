# Generated by Django 2.0.6 on 2018-06-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallthings', '0010_auto_20180621_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='image',
            field=models.ImageField(default='images/def.jpg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='newpost',
            name='thumb',
            field=models.ImageField(default='thumbs/def.jpg', upload_to='images'),
        ),
    ]