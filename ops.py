"""Operations module for <Django Project Name>

Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""
from paver.easy import *
import sys

from glob import glob

class DependencyNeeded(Exception):
    pass

def have(name):
    return ('command not found' not in
            sh(name, capture=True, ignore_error=True) )

def software(name):
    def missing():
        raise DependencyNeeded('Please install %s first '
                               'using your package manager' % name)

    if have(name):
        return ''
    elif sys.platform == 'darwin':
        if have('brew'):
            path = glob('/usr/local/Cellar/%s/**/bin' % name)
            if path:
                return 'PATH=%s:$PATH' % path[0]
            missing()
        else:
            raise DependencyNeeded('Please install homebrew: '
                                   'http://mxcl.github.com/homebrew/')
    elif sys.platform.startswith('linux'):
        missing()
