# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from .validators import eth_address_validator


class DonationUserAddress(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True,
                             verbose_name=_("Пользователь"),
                             related_name="addresses")

    e20_wallet = models.CharField(_("Адрес для получения токенов"),
                                  max_length=50,
                                  validators=[eth_address_validator])

    created_dt = models.DateTimeField(_("Дата создания"),
                                      auto_now_add=True)

    class Meta:
        verbose_name = _("Адрес пользователя")
        verbose_name_plural = _("Адреса пользователей")

    def __unicode__(self):
        return self.e20_wallet


class Donation(models.Model):

    class PAYMENT_METHOD:
        ETH = 'ETH'
        BTC = 'BTC'
        LTC = 'LTC'
        ETC = 'ETC'

        CHOICES = (
            (ETH, ETH),
            (BTC, BTC),
            (LTC, LTC),
            (ETC, ETC)
        )

        TX_ADDRESSES = {
            ETH: "https://etherscan.io/tx/{}",
            BTC: "https://blockchain.info/tx/{}",
            LTC: "https://live.blockcypher.com/ltc/tx/{}/",
            ETC: "https://gastracker.io/tx/{}"
        }

    payment_method = models.CharField(_("Тип оплаты"),
                                      max_length=3,
                                      choices=PAYMENT_METHOD.CHOICES)

    donation_address = models.CharField(_("Адрес оплаты"),
                                        max_length=50)

    e20_wallet = models.CharField(_("Адрес для получения токенов"),
                                  max_length=50,
                                  validators=[eth_address_validator])

    tx_id = models.CharField(_("Номер транзакции"),
                             max_length=100,
                             blank=True,
                             null=True)

    tokens = models.FloatField(_("Количество токенов"),
                               blank=True,
                               null=True)
    tx_sum = models.FloatField(_("Сумма транзакции"),
                               blank=True,
                               null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True,
                             verbose_name=_("Пользователь"),
                             related_name="donations")

    created_dt = models.DateTimeField(_("Дата создания"),
                                      auto_now_add=True)

    class Meta:
        verbose_name = _("Транзакция")
        verbose_name_plural = _("Транзакции")

    def __unicode__(self):
        return self.tx_id

    @property
    def tx_link(self):
        return self.PAYMENT_METHOD.TX_ADDRESSES[
            self.payment_method].format(self.tx_id)
