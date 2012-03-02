# -*- coding: utf-8 -*-
"""
Local development settings.

Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""

import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jacob Oscarson', 'jacob@plexical.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.abspath(os.path.join(PROJECT_DIR,
                                             '..', 'var', 'dev.db')),
    }
}

"""
Absolute filesystem path to the directory that will hold user-uploaded files.
Example: `"/home/media/media.lawrence.com/`
"""
MEDIA_ROOT = os.path.join(PROJECT_DIR, '..', 'static', 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(PROJECT_DIR, '..', 'static')),
)

"""
Make this unique, and don't share it with anybody.
"""
SECRET_KEY = 'my-supersecret-developer-key'

"""
Per environment specific apps.
Relevant place to put development environment specific installed apps.
"""
EXTRA_APPS = (
    'django_pytest',
    'werkzeug_debugger_runserver'
)

TEST_RUNNER = 'django_pytest.test_runner.run_tests'
