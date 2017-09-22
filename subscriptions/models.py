# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscription(models.Model):
    name = models.CharField('Имя подписчика',
                            max_length=128)
    email = models.EmailField('Email подписчика')
    subscribed_date = models.DateTimeField('Дата подписки',
                                           auto_now_add=True)

    class Meta:
        verbose_name = 'Подписка на новости'
        verbose_name_plural = 'Подписки на новости'

    def __unicode__(self):
        return self.email

