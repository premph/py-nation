# Generated by Django 2.0.6 on 2018-06-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallthings', '0020_auto_20180624_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcomment',
            name='created_date',
            field=models.DateField(),
        ),
    ]