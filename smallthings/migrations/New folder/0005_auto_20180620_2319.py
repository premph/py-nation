# Generated by Django 2.0.6 on 2018-06-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallthings', '0004_auto_20180620_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='image',
            field=models.ImageField(default='b2.jpg', upload_to='images'),
        ),
    ]