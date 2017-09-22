# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import MenuItem
from subscriptions.forms import SubscriptionForm

# Create your views here.


class IndexView(TemplateView):
    def __init__(self, **kwargs):
        self.template_name = "index_old.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['menu'] = MenuItem.objects.all()
        context['subscribe_form'] = SubscriptionForm()
        return context