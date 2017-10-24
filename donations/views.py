# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils.translation import ugettext as _
from .validators import eth_address_validator


@csrf_exempt
@require_POST
@login_required
def check_eth_address(request):

    if not request.is_ajax():
        return HttpResponseBadRequest()

    try:
        eth_address_validator(request.POST.get('e20_wallet'))
        resp = "true"
    except ValidationError:
        resp = _("Enter valid ethereum address")

    return JsonResponse(resp, safe=False)
