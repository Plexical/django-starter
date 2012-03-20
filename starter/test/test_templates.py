import re
import pytest

from starter.test.support import render_raw, render_to_soup

def pytest_funcarg__base(request):
    def setup():
        return render_to_soup('base.html', marker='marker')
    return request.cached_setup(setup)

def pytest_generate_tests(metafunc):
    if 'base_uri' in metafunc.funcargnames:
        base = render_to_soup('base.html', marker='marker')
        def walk(pg):
            for node in pg.recursiveChildGenerator():
                attrs = dict(getattr(node, 'attrs', {}))
                uri = attrs.get('src') or attrs.get('href')
                if uri and uri.startswith('/static'):
                    yield uri
        metafunc.parametrize('base_uri', list(walk(base)))

def test_base_sanity(base):
    assert base.find(text=re.compile('marker')) == ' marker '

def test_base_res(client, base_uri):
    assert client.get(base_uri).status_code == 200, base_uri
