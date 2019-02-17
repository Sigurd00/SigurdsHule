# Generated by Django 2.1.2 on 2018-11-03 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20181103_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projekter',
            name='file',
        ),
        migrations.AddField(
            model_name='projekter',
            name='img_code',
            field=models.ImageField(blank=True, upload_to='projectImages/code'),
        ),
        migrations.AddField(
            model_name='projekter',
            name='img_looks',
            field=models.ImageField(blank=True, upload_to='projectImages/looks'),
        ),
        migrations.AlterField(
            model_name='projekter',
            name='oprettet',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 11, 3, 14, 55, 15, 691642, tzinfo=utc)),
        ),
    ]