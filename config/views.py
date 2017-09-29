# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


from subscriptions.forms import SubscriptionForm
from .models import SiteConfiguration
from .mixins import MenuContextMixin
from .forms import SignUpForm

# Create your views here.


class IndexView(MenuContextMixin, TemplateView):
    def __init__(self, **kwargs):
        config = SiteConfiguration.get_solo()
        if config.show_site:
            self.template_name = "index_main.html"
        else:
            self.template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        config = SiteConfiguration.get_solo()
        if config.show_site:
            context['subscribe_form'] = SubscriptionForm()
        return context


class SignupView(MenuContextMixin, FormView):
    template_name = "signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        return redirect('index')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super(SignupView, self).dispatch(request, *args, **kwargs)


class CustomLoginView(MenuContextMixin, LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    """View for logout"""

    logout(request)

    return redirect('index')


class PersonalProfileView(MenuContextMixin, TemplateView):
    template_name = "personal_profile.html"
