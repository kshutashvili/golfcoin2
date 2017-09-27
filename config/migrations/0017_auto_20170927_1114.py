# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_auto_20170927_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link',
            field=models.FileField(upload_to='whitepapers', verbose_name='Whitepaper'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link_en',
            field=models.FileField(null=True, upload_to='whitepapers', verbose_name='Whitepaper'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link_ru',
            field=models.FileField(null=True, upload_to='whitepapers', verbose_name='Whitepaper'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link_zh',
            field=models.FileField(null=True, upload_to='whitepapers', verbose_name='Whitepaper'),
        ),
    ]
