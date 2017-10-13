# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (_("Contacts"),
             {'fields': ('address',
                         'phone_number')}),
            (_("Document scans"),
             {'fields': ('document_1',
                         'document_2',
                         'document_3')}
             ),
    )


admin.site.register(User, MyUserAdmin)

