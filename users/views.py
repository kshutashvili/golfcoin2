# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import magic
from django.conf import settings
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
        url = os.path.join('/media/', filename)
        path = os.path.join(settings.MEDIA_ROOT, filename)
        mime = magic.Magic(mime=True)
        cont_type = mime.from_file(path)
        response['Content-Type'] = cont_type
        response['X-Accel-Redirect'] = url
        return response
    else:
        return HttpResponseForbidden(_("Restricted Access"))
