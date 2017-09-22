# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import MenuItem
from subscriptions.forms import SubscriptionForm
from .models import SiteConfiguration

# Create your views here.


class IndexView(TemplateView):
    def __init__(self, **kwargs):
        config = SiteConfiguration.get_solo()
        if config.show_site:
            self.template_name = "index_main.html"
        else:
            self.template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['menu'] = MenuItem.objects.all()
        config = SiteConfiguration.get_solo()
        if config.show_site:
            context['subscribe_form'] = SubscriptionForm()
        return context