from django.urls import re_path, include
from django.views.generic.base import TemplateView

from .forms import DemoForm


urlpatterns = [
    re_path(
        r'^$',
        TemplateView.as_view(template_name='demo.html'),
        {'form': DemoForm()},
        name='demo',
        ),
    re_path(r'^markitup/', include('markitup.urls')),
]
