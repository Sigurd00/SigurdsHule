# Generated by Django 2.1.2 on 2018-11-03 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20181103_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekter',
            name='media',
            field=models.CharField(blank=True, default='non', max_length=20),
        ),
        migrations.AlterField(
            model_name='projekter',
            name='oprettet',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 3, 12, 33, 58, 282026)),
        ),
    ]