import os, sys

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    from starter import meta
    os.environ['DJANGO_SETTINGS_MODULE'] = 'starter.develop'
    sys.path.insert(0, meta.path())

from django_pytest.conftest import *
