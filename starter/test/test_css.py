import os
import re

from glob import glob
from contextlib import closing

import pytest

from starter.shortcuts import path

def uris(css):
    with closing(open(css)) as fp:
        for lineno, line in enumerate(fp):
            if not line.startswith('/*'):
                line = line.strip()
                matches = re.findall("url\((.*?)\)", line)
                if matches:
                    for match in matches:
                        # Doubly screwed according to Thorvalds ;-)
                        yield css, lineno, match.strip("\"'")

def stylesheets():
    from django.conf import settings
    return glob(path(settings.STATIC_ROOT, '..', '..', 'static', 'css', '*')) # XXX

def pytest_generate_tests(metafunc):
    if 'resinfo' in metafunc.funcargnames:
        for css in stylesheets():
            metafunc.parametrize('resinfo', uris(css))

def test_url_resource(resinfo, client):
    css, lineno, uri = resinfo
    complain = '%s not found in %s:%s' % (uri, css, lineno)
    assert client.get(uri).status_code == 200, complain
