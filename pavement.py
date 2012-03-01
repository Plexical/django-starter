# -*- coding: utf-8 -*-
"""pavement.py -- pavement for <Django Project Name>

Copyright 2011 Plexical. See LICENCE for permissions.
"""
import os
import sys

from paver.easy import *

try:
    from starter import meta
except ImportError:
    sys.path.append('.')
    from starter import meta

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

@task
def watch():
    sh('compass watch --sass-dir=scss --css-dir=static/css &')
    # sh('coffee -cwlo static/js coffee/ &')

@task
def unwatch():
    sed = 'sed \'/bin\/coffee/p; /grep/d;\''
    awk = 'awk \'{print $1}\''
    sh("ps | grep coffee | %s | %s | xargs kill -TERM" % (sed, awk))
    sed = 'sed \'/bin\/compass/p; /grep/d;\''
    sh('ps | grep compass | %s | %s | xargs kill -TERM' % (sed, awk))

@needs('unwatch', 'watch')
def rewatch():
    pass

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
