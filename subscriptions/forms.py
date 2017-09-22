# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name', 'email',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'name', 'placeholder': u'Введите свое имя*'}
        self.fields['email'].widget.attrs = {'class': 'email', 'placeholder': u'Введите свой e-mail*'}
