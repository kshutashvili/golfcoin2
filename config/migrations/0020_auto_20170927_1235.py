# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0019_auto_20170927_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='how_block_video',
            field=models.URLField(default='', verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'How it works'"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='how_block_video_de',
            field=models.URLField(null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'How it works'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='how_block_video_en',
            field=models.URLField(null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'How it works'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='how_block_video_es',
            field=models.URLField(null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'How it works'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='how_block_video_ru',
            field=models.URLField(null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'How it works'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='how_block_video_zh',
            field=models.URLField(null=True, verbose_name="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'How it works'"),
        ),
    ]
