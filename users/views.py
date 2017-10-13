# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.http.response import HttpResponse, HttpResponseForbidden
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


def document_view(request, filename):

    """Allow to download files only for authorized users"""

    # try to get document obj and check its owner
    filename = os.path.join('scans/', filename)
    document_obj = User.objects.filter(
        Q(document_1=filename) |
        Q(document_2=filename) |
        Q(document_3=filename)
    ).first()

    if document_obj and (document_obj == request.user or request.user.is_superuser):
        response = HttpResponse()
        response['X-Accel-Redirect'] = os.path.join('/media/', filename)
        return response
    else:
        return HttpResponseForbidden(_("Restricted Access"))
