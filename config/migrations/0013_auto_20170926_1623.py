# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0012_siteconfiguration_timer_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u0432 \u043a\u043d\u043e\u043f\u043a\u0435 'Whitepaper'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u0432 \u043a\u043d\u043e\u043f\u043a\u0435 'Whitepaper'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='main_block_whitepaper_link_zh',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u0432 \u043a\u043d\u043e\u043f\u043a\u0435 'Whitepaper'"),
        ),
    ]
