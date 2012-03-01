# -*- coding: utf-8 -*-
"""
Installs <Django Project Name>
------------------------------

Copyright 2011 Plexical. See LICENCE for permissions.
"""
import os
import sys
import subprocess

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if 'boot' in sys.argv:
    if not os.path.exists(os.path.join('bin', 'pip')):
        sys.path.insert(0, 'virtualenv.zip')
        import virtualenv
        print('Creating virtualenv..')
        virtualenv.create_environment('.')
        subprocess.call('./bin/pip install paver', shell=True)
        print('done.')
    else:
        print('Virtualenv already set up')
    sys.exit(0)

try:
    from starter import meta
except ImportError:
    sys.path.append('.')
    from starter import meta

setup(
    name=meta.name,
    packages=(meta.name),
    version=meta.version,
    author='Jacob Oscarson',
    author_email='jacob@plexical.com',
    install_requires=open('requirements.txt').readlines()
)

try:
    import paver
    from pavement import *
except ImportError:
    pass
