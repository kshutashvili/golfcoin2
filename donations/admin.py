# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import DonationUserAddress, Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass


@admin.register(DonationUserAddress)
class DonationUserAddressAdmin(admin.ModelAdmin):
    pass
