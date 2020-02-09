CHANGES
=======

3.5.0 (2020.02.09)
-------------------

* Add support for Django 1.11 and 2.0.

3.0.0 (2016.09.04)
------------------

* Drop support for Python 3.3.
* Drop compatibility with Django < 1.8.

2.3.1 (2016.02.06)
------------------

* Use protocol-less URL for externally hosted jQuery to avoid browser warnings.


2.3.0 (2016.01.17)
------------------

* Template tags now support Django's STATICFILES_STORAGE setting.
  Thanks Ivan Ven Osdel for report and fix.
* Added ``render_with`` method to render a MarkupField with a different filter.
* Dropped compatibility with Django < 1.7.
* Compatibility with Django 1.8 and 1.9. Thanks Ivan Ven Osdel for the fixes!
* Dropped compatibility with Python 2.6.
* Added support for Python 3.5.


2.2.2 (2014.09.08)
------------------

* Adapted MarkupField to work with Django 1.7 migrations. Merge of
  BB-15. Thanks Neil Muller for report and fix.

2.2.1 (2014.07.15)
------------------

* Fixed regression under Python 2 with MARKITUP_FILTER and
  MARKITUP_PREVIEW_FILTER. Thanks Berker Peksag and Neil Muller for the report,
  and Neil Muller for the fix.


2.2 (2014.07.03)
----------------

* Added Python 3.3+ support. Thanks Berker Peksag.


2.1 (2013.11.11)
----------------

* Updated default jQuery version from 1.6 to 2.0.3.

* Fixed ``MARKITUP_AUTO_PREVIEW``; the "fix" in 2.0 was wrong and broke it.


2.0 (2013.11.06)
----------------

* Fixed ``MARKITUP_AUTO_PREVIEW``; MarkItUp! now observes mousedown events, not
  mouseup. Thanks Alexandr Shurigin.

* Added support for Django 1.6.

* BACKWARDS-INCOMPATIBLE: Dropped support for Python 2.5 and Django 1.3.

1.1.0 (2013.04.26)
------------------

- Updated to MarkItUp! 1.1.14 and fixed compatibility with jQuery 1.9. Thanks
  Roman Akinfold!

- Fixed MarkItUpWidget with custom attrs. Thanks GeyseR.

- Set previewParserPath dynamically rather than requiring it to be set in
  ``set.js``.  Thanks Sebastian Brandt.

- Fixed hidden-widget rendering of a ``MarkupField``. Thanks Aramgutang.

- Prevented double application of MarkItUp! editor to an
  element. Fixes #4. Thanks Rich Leland.

- Added `__len__` to `Markup` object to facilitate length and truthiness checks
  in templates. Fixes #16. Thanks Edmund von der Burg.

1.0.0 (2011.07.11)
------------------

- Removed all compatibility shims for Django versions prior to 1.3, including
  all support for static media at ``MEDIA_URL``, static assets under
  ``media/``, and the ``MARKITUP_MEDIA_URL`` setting.

- Updated to jquery 1.6.

- Added check to avoid double _rendered fields when MarkupField is used on an
  abstract base model class. Fixes #11. Thanks Denis Kolodin for report and
  patch.

- Added compatibility with new AJAX CSRF requirements in Django 1.2.5 and
  1.3. Fixes #7. Thanks zw0rk for the report.

- Added blank=True to MarkupField's auto-added rendered-field to avoid South
  warnings.

- Django 1.3 & staticfiles compatibility: MARKITUP_MEDIA_URL and jQuery URL
  default to STATIC_URL rather than MEDIA_URL, if set.  Static assets now
  available under static/ as well as media/.  Thanks Mikhail Korobov.

- MarkupField.get_db_prep_value updated to take "connection" and "prepared"
  arguments to avoid deprecation warnings under Django 1.3.  Thanks Mikhail
  Korobov.

- enforce minimum length of 3 characters for MarkItUp!-inserted h1 and h2
  underline-style headers (works around bug in python-markdown).  Thanks
  Daemian Mack for the report.

0.6.1 (2010.07.01)
------------------

- Added markitup set for reST. Thanks Jannis Leidel.

- fixed reST renderer to not strip initial headline. Thanks Jannis Leidel.

- prevent mark_safe from mangling Markup objects.

0.6.0 (2010.04.26)
------------------

- remove previously-deprecated markitup_head template tag

- wrap jQuery usage in anonymous function, to be more robust against other
  JS framework code on the page (including other jQuerys).  Thanks Mikhael
  Korneev.

- upgrade to MarkItUp! 1.1.7

- add render_markup template filter

- update to jQuery 1.4 and MarkItUp! 1.1.6

- Add auto_preview option.

- Ajax preview view now uses RequestContext, and additionally passes
  ``MARKITUP_MEDIA_URL`` into the template context. (Previously,
  ``MARKITUP_MEDIA_URL`` was passed as ``MEDIA_URL`` and
  RequestContext was not used). Backwards-incompatible; may require
  change to preview template.

0.5.2 (2009.11.24)
------------------

- Fix setup.py so ``tests`` package is not installed.

0.5.1 (2009.11.18)
------------------

- Added empty ``models.py`` file so ``markitup`` is properly registered in
  ``INSTALLED_APPS``. Fixes issue with ``django-staticfiles`` tip not
  finding media.

0.5 (2009.11.12)
----------------

- Added ``MarkupField`` from http://github.com/carljm/django-markupfield
  (thanks Mike Korobov)

- Deprecated ``markitup_head`` template tag in favor of ``markitup_media``.

- Added ``MARKITUP_MEDIA_URL`` setting to override base of relative media
  URL paths.

0.3 (2009.11.04)
----------------

- added template-tag method for applying MarkItUp! editor (inspired by
  django-wysiwyg)

0.2 (2009.03.18)
----------------

- initial release

