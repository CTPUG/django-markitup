from setuptools import setup


long_description = (open('README.rst').read() +
                    open('CHANGES.rst').read() +
                    open('TODO.rst').read())

def _static_files(prefix):
    return [prefix+'/'+pattern for pattern in [
        'markitup/*.*',
        'markitup/sets/*/*.*',
        'markitup/sets/*/images/*.png',
        'markitup/skins/*/*.*',
        'markitup/skins/*/images/*.png',
        'markitup/templates/*.*'
    ]]

setup(
    name='django-markitup',
    version='4.1.0',
    description='Markup handling for Django using the MarkItUp! universal markup editor',
    long_description_content_type="text/x-rst",
    long_description=long_description,
    author='Carl Meyer',
    author_email='carl@oddbird.net',
    url='https://github.com/CTPUG/django-markitup',
    packages=['markitup', 'markitup.templatetags'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
    ],
    zip_safe=False,
    test_suite='runtests.runtests',
    tests_require='Django>=1.11',
    package_data={'markitup': ['templates/markitup/*.html'] +
                              _static_files('static')}
)
