# -*- coding: utf-8 -*-
"""pavement.py -- pavement for <Django Project Name>

Copyright 2011 Plexical. See LICENCE for permissions.
"""
import os
import sys

from paver.easy import *

@task
def dropdb():
    "Drops the local development database"
    path('var/dev.db').remove()

def script(name, *lines):
    path('bin/%s' % name).write_lines(
        ("#!/bin/sh", "ME=$(dirname $0)") + lines)
    sh('chmod +x bin/%s' % name)

@task
def scripts():
    "Creates utility scripts for manage.py, run local server and test runner"
    script('manage',
           "$ME/../bin/python $ME/../%s/manage.py $@" % meta.name)
    script('run',
           "$ME/../bin/python $ME/../%s/manage.py runserver $@" % meta.name)
    script('test',
           "(cd $ME/.. &&",
           "./bin/python %s/manage.py test %s $@)" % (meta.name,
                                                      meta.name) )

@needs('scripts')
@task
def env():
    "Ensure virtualenv exists and is up to date"
    sh('./bin/pip install -r requirements.txt')
    sh('./bin/pip install -r deps/developer.txt')

@needs('dropdb')
@task
def clean():
    "Removes ALL locally generated files"
    path('bin').rmtree()
    path('lib').rmtree()
    path('include').rmtree()
