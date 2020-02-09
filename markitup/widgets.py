from __future__ import unicode_literals

import posixpath
from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.template.loader import render_to_string
try:
    from django.urls import NoReverseMatch, reverse
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.safestring import mark_safe
from markitup import settings
from markitup.util import absolute_url



class MarkupInput(forms.Widget):
    def render(self, name, value, attrs=None):
        if value is not None:
            # Special handling for MarkupField value.
            # This won't touch simple TextFields because they don't have
            # 'raw' attribute.
            try:
                value = value.raw
            except AttributeError:
                pass
        return super(MarkupInput, self).render(name, value, attrs)


class MarkupTextarea(MarkupInput, forms.Textarea):
    pass


class MarkupHiddenWidget(MarkupInput, forms.HiddenInput):
    pass


class MarkItUpWidget(MarkupTextarea):
    """
    Widget for a MarkItUp editor textarea.

    Takes two additional optional keyword arguments:

    ``markitup_set``
        URL path (absolute or relative to STATIC_URL) to MarkItUp
        button set directory.  Default: value of MARKITUP_SET setting.

    ``markitup_skin``
        URL path (absolute or relative to STATIC_URL) to MarkItUp skin
        directory.  Default: value of MARKITUP_SKIN setting.

    """
    def __init__(self, attrs=None,
                 markitup_set=None,
                 markitup_skin=None,
                 auto_preview=None):
        self.miu_set = absolute_url(markitup_set or settings.MARKITUP_SET)
        self.miu_skin = absolute_url(markitup_skin or settings.MARKITUP_SKIN)
        if auto_preview is None:
            auto_preview = settings.MARKITUP_AUTO_PREVIEW
        self.auto_preview = auto_preview
        super(MarkItUpWidget, self).__init__(attrs)

    def _media(self):
        js_media = [absolute_url(settings.JQUERY_URL)] if settings.JQUERY_URL is not None else []
        js_media = js_media + [absolute_url('markitup/ajax_csrf.js'),
                               absolute_url('markitup/jquery.markitup.js'),
                               posixpath.join(self.miu_set, 'set.js')]
        return forms.Media(
            css={'screen': (posixpath.join(self.miu_skin, 'style.css'),
                            posixpath.join(self.miu_set, 'style.css'))},
            js=js_media)
    media = property(_media)

    def render(self, name, value, attrs=None):
        html = super(MarkItUpWidget, self).render(name, value, attrs)

        # Passing base_attrs as a kwarg for compatibility with Django < 1.11
        # (where it will be treated as an innocuous attr named base_attrs)
        final_attrs = self.build_attrs(
            base_attrs=self.attrs, extra_attrs=attrs)

        try:
            preview_url = reverse('markitup_preview')
        except NoReverseMatch:
            preview_url = ""

        html += render_to_string('markitup/editor.html',
                                 {'textarea_id': final_attrs['id'],
                                 'AUTO_PREVIEW': self.auto_preview,
                                 'preview_url': preview_url})

        return mark_safe(html)


class AdminMarkItUpWidget(MarkItUpWidget, AdminTextareaWidget):
    """
    Add vLargeTextarea class to MarkItUpWidget so it looks more
    similar to other admin textareas.

    """
    pass
