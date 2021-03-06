# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0002_video_video_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='time of download start')),
                ('success', models.BooleanField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeper.Video')),
            ],
        ),
    ]
