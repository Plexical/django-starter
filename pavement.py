# -*- coding: utf-8 -*-
"""pavement.py -- pavement for <Django Project Name>

Copyright 2011 Plexical. See LICENCE for permissions.
"""
import os
import sys

from paver.easy import *
from paver.setuputils import setup

from starter import meta

setup(
    name=meta.name,
    packages=(meta.name),
    version=meta.version,
    author='Jacob Oscarson',
    author_email='jacob@plexical.com',
    install_requires=open(os.path.join('deps',
                                       'run.txt')).readlines()
)

@task
def virtualenv():
    "Prepares a checked out directory for development"
    if not os.path.exists(os.path.join('bin', 'pip')):
        sys.path.insert(0, os.path.join('deps', 'virtualenv.zip'))
        import virtualenv
        virtualenv.create_environment('.')
    else:
        print('Virtualenv already set up')

def script(name, *lines):
    path('bin/%s' % name).write_lines(
        ("#!/bin/sh", "ME=$(dirname $0)") + lines)
    sh('chmod +x bin/%s' % name)

@task
def scripts():
    script('manage',
           "$ME/../bin/python $ME/../%s/manage.py $@" % meta.name)
    script('run',
           "$ME/../bin/python $ME/../%s/manage.py runserver $@" % meta.name)
    script('test',
           "(cd $ME/.. &&",
           "./bin/python %s/manage.py test %s $@)" % (meta.name,
                                                      meta.name) )

@needs('virtualenv', 'scripts')
@task
def env():
    "Ensure virtualenv exists and is up to date"
    sh('./bin/pip install -r deps/run.txt')
    sh('./bin/pip install -r deps/developer.txt')

@task
def clean():
    path('bin').rmtree()
    path('lib').rmtree()
    path('include').rmtree()
