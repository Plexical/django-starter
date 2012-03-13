# -*- coding: utf-8 -*-
"""
Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""
import os

name = 'starter'
version = '0.1'

def path(*segs):
    from django.conf import settings
    return os.path.abspath(os.path.join(settings.PROJECT_DIR, *segs))
