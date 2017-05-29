# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailffa', '0003_cron'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cron',
            name='job',
        ),
        migrations.AddField(
            model_name='job',
            name='job_cron',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cron',
        ),
    ]