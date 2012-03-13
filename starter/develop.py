# -*- coding: utf-8 -*-
"""
Local development settings.

Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""
import os

from starter.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ENV = 'dev'

ADMINS = (
    ('Foo Bar', 'foo@example.com'),
)

MANAGERS = ADMINS

"""
This server's own opinion of it's name.
"""
INSTANCE_URL = 'http://localhost:8000'

ADMINS = (
    ('Jacob Oscarson', 'jacob@plexical.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path(PROJECT_DIR, '..', 'var', 'dev.db'),
    }
}

"""
Absolute filesystem path to the directory that will hold user-uploaded files.
Example: `"/home/media/media.lawrence.com/`
"""
MEDIA_ROOT = path(PROJECT_DIR, '..', 'static', 'media')

STATIC_ROOT = path(PROJECT_DIR, 'static')

STATICFILES_DIRS = (
    path(PROJECT_DIR, '..', 'static'),
)

"""
Make this unique, and don't share it with anybody.
"""
SECRET_KEY = 'my-supersecret-developer-key'

"""
Per environment specific apps.
Relevant place to put development environment specific installed apps.
"""
INSTALLED_APPS = BASE_INSTALLED_APPS + (
    'django_pytest',
    'werkzeug_debugger_runserver'
)

TEST_RUNNER = 'django_pytest.test_runner.run_tests'
