# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Subscription
from .forms import SubscriptionForm


class SubscriptionView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        subscribe_form = SubscriptionForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
        return redirect(self.success_url)
