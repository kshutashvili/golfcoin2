# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20170922_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_date1',
            field=models.DateField(blank=True, null=True, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0434\u0430\u0442\u0430)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_date2',
            field=models.DateField(blank=True, null=True, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0434\u0430\u0442\u0430)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_date3',
            field=models.DateField(blank=True, null=True, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0434\u0430\u0442\u0430)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_date4',
            field=models.DateField(blank=True, null=True, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0434\u0430\u0442\u0430)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_date5',
            field=models.DateField(blank=True, null=True, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0434\u0430\u0442\u0430)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_date6',
            field=models.DateField(blank=True, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0434\u0430\u0442\u0430)'),
        ),
    ]
