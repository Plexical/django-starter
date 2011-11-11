# -*- coding: utf-8 -*-
"""
Copyright 2011 Plexical. See LICENCE for permissions.
"""
import os

name = 'starter'
version = '0.1'

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'starter.settings'

def path(*segs):
    from django.conf import settings
    return os.path.abspath(os.path.join(settings.PROJECT_DIR, *segs))
