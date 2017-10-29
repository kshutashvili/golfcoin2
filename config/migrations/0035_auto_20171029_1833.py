# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0034_auto_20171013_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='logo_footer',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='Footer logo'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='logo_header_main',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='Site header logo'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='logo_header_profile',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='Profile pages header logo'),
        ),
    ]
