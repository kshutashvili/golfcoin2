# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0030_merge_20171005_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='discount_block_html_id',
            field=models.CharField(default='presale', max_length=16, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 HTML'),
        ),
        migrations.AddField(
            model_name='teammate',
            name='social_facebook',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='teammate',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Linkedin'),
        ),
    ]
