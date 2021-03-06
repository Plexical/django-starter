# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

from django.template import loader, Context, Template

run_template = lambda t, **kw: Template(t).render(Context(kw))
soup_template = lambda t, **kw: BeautifulSoup(run_template(t, **kw))

def render_raw(name, **ctx):
    return loader.render_to_string(name, ctx)

def render_to_soup(name, **ctx):
    return BeautifulSoup(render_raw(name, **ctx))

def fake_get(path='/', user=None):
    from django.test.client import RequestFactory
    from django.contrib.auth.models import AnonymousUser

    req = RequestFactory().get(path)
    req.user = AnonymousUser() if user is None else user
    req.current_page = 'dummy'

    return req

def resource_walk(dom):
    for node in dom.recursiveChildGenerator():
        attrs = dict(getattr(node, 'attrs', {}))
        uri = attrs.get('src') or attrs.get('href')
        if uri and uri.startswith('/static'):
            yield uri
