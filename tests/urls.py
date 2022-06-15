from __future__ import unicode_literals

from django.urls import re_path, include

urlpatterns = [
    re_path(r'^markitup/', include('markitup.urls')),
]
