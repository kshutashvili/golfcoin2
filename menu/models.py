# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MenuItem(models.Model):
    name = models.CharField('Название',
                            max_length=50)
    link = models.CharField('Ссылка',
                            max_length=255,
                            help_text='#about or #follow',
                            blank=True)
    order = models.IntegerField('Порядок',
                                default=0)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order',]

    def __unicode__(self):
        return self.name
