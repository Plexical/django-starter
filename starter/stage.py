# -*- coding: utf-8 -*-
"""
Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""
import os

from starter.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ENV = 'stage'

ADMINS = (
    ('Foo Bar', 'foo@example.com'),
)

MANAGERS = ADMINS

SECRET_KEY = 'T' # XXX must fill in

"""
This server's own opinion of it's name.
"""
INSTANCE_URL = 'T'

"""
Media files root.
"""
MEDIA_ROOT = 'T' # XXX must be filled in

"""
Static files root.
"""
STATIC_ROOT = 'T' # XXX must be filled in

INSTALLED_APPS = BASE_INSTALLED_APPS
