"""golfco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import RegexURLPattern
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views
from config.views import (IndexView, SignupView,
                          logout_view, CustomLoginView,
                          PersonalProfileView, check_email,
                          check_email_profile, get_tokens_count)
from subscriptions.views import SubscriptionView
from two_factor.urls import urlpatterns as two_factor_urls
from users.views import document_view
from donations.views import check_eth_address

decorators = [user_passes_test(lambda u: u.is_superuser)]


def decorate_pattern(urlpattern):
    callback = urlpattern.callback
    for decorator in reversed(decorators):
        callback = decorator(callback)

    return RegexURLPattern(
        urlpattern.regex.pattern,
        callback,
        urlpattern.default_args,
        urlpattern.name
    )

two_factor_urls = [two_factor_urls[0]] + [decorate_pattern(pattern) for pattern in two_factor_urls[1:]]

urlpatterns = i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'', include(two_factor_urls, 'two_factor')),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', CustomLoginView.as_view(), name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^profile/$', PersonalProfileView.as_view(), name='profile'),
    url(r'^subscription/$', SubscriptionView.as_view(), name='subscription'),
    url(r'^check_email/$', check_email, name='check_email'),
    url(r'^check_email_profile/$', check_email_profile, name='check_email_profile'),
    url(r'^check_eth_address/$', check_eth_address, name='check_eth_address'),
    url(r'^get_tokens_count/$', get_tokens_count, name="tokens_count"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'document/(?P<filename>[^/]+)$',
        document_view,
        name='document_view'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += i18n_patterns(
        url(r'^rosetta/', include('rosetta.urls')),
    )
