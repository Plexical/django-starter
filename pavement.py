# -*- coding: utf-8 -*-
"""pavement.py -- pavement for <Django Project Name>

Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""
import os
import sys

from paver.easy import *

try:
    from starter import meta
    import ops
except ImportError:
    sys.path.append('.')
    from starter import meta
    import ops

@task
def dropdb():
    "Drops the local development database"
    path('var/dev.db').remove()

@task
def syncdb():
    "Runs syncdb"
    sh('./bin/manage syncdb --noinput')

@needs('dropdb')
@task
def freshdb():
    "Re-creates the development database"
    syncdb()

def script(name, *lines):
    path('bin/%s' % name).write_lines(
        ("#!/bin/sh", "ME=$(dirname $0)") + lines)
    sh('chmod +x bin/%s' % name)

@task
def scripts():
    "Creates utility scripts for manage.py, run local server and test runner"
    script('manage',
           "$ME/../bin/python $ME/../%s/manage.py $@ "
           "--settings=starter.develop" % meta.name)
    script('run',
           ("$ME/../bin/python $ME/../%s/manage.py "
            "runserver --settings=starter.develop 0.0.0.0:8000 $@" %
            meta.name))
    script('test',
           "(cd $ME/.. &&",
           "./bin/python %s/manage.py test %s "
           "--settings=starter.develop $@)" % (meta.name,
                                               meta.name) )
    script('bundle',
           "(cd $ME/.. &&",
           "./bin/paver bundle)")

@task
def compass():
    ops.check('compass version')
    sh('compass compile --sass-dir=scss --css-dir=static/css')

@task
def coffee():
    ops.check('coffee -v')
    sh('coffee -cl static/js/')

@task
def wr_installed():
    ops.check('wr -V')

@needs('wr_installed')
@task
def watch():
    "Watch for SASS and CoffeeScript"
    sh("(cd scss && wr ../bin/bundle) &")
    sh("(cd static && wr ../bin/bundle) &")

@needs('compass', 'coffee')
@task
def transpile():
    "Run SASS and coffeescript compilers"

@needs('transpile')
@task
def bundle():
    "Bundle Js /w browserify"
    # Example
    sh('browserify -e static/js/starter.js -o static/js/starter.bundle.js')

@task
def unwatch():
    "Stop SASS and CoffeeScript watchers"
    sh("ps | grep wr | sed '/grep/d' | awk '{print $1}' | xargs kill -TERM")

@needs('unwatch', 'watch')
def rewatch():
    "Restarts SASS and CoffeeScript watchers"
    pass

@task
def messages():
    path = ops.software('gettext')
    sh("cd starter && %s ../bin/manage makemessages -a" % path)

@task
def translate():
    path = ops.software('gettext')
    sh("cd starter && %s ../bin/manage compilemessages" % path)

@needs('scripts')
@task
def env():
    "Ensure virtualenv exists and is up to date"
    sh('./bin/pip install -r requirements.txt')
    sh('./bin/pip install -r development.txt')

@needs('dropdb')
@task
def clean():
    "Removes ALL locally generated files"
    path('bin').rmtree()
    path('lib').rmtree()
    path('include').rmtree()
