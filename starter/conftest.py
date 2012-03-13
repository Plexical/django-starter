import os, sys

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    from starter import meta
    sys.path.insert(0, meta.path())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'starter.develop'

from django_pytest.conftest import *
