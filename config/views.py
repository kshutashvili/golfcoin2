# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http.response import JsonResponse, HttpResponseBadRequest

from django.utils.translation import ugettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters


from subscriptions.forms import SubscriptionForm
from .models import SiteConfiguration
from .forms import SignUpForm


class IndexView(TemplateView):
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


class SignupView(FormView):
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


class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    """View for logout"""

    logout(request)

    return redirect('index')


class PersonalProfileView(TemplateView):
    template_name = "personal_profile.html"


@csrf_exempt
def check_email(request):

    if not request.is_ajax():
        return HttpResponseBadRequest()

    User = get_user_model()

    if User.objects.filter(email__iexact=request.POST.get('email')).count() > 0:
        ret = _("This email address is already registered")
    else:
        ret = "true"

    return JsonResponse(ret, safe=False)
