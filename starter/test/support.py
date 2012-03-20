# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

from django.template import loader, Context, Template

run_template = lambda t, **kw: Template(t).render(Context(kw))
soup_template = lambda t, **kw: BeautifulSoup(run_template(t, **kw))

def render_raw(name, **ctx):
    from sekizai.context import SekizaiContext
    return loader.render_to_string(name, SekizaiContext(ctx))

def render_to_soup(name, **ctx):
    return BeautifulSoup(render_raw(name, **ctx))

def fake_get(path='/', user=None):
    from django.test.client import RequestFactory
    from django.contrib.auth.models import AnonymousUser

    req = RequestFactory().get(path)
    req.user = AnonymousUser() if user is None else user
    req.current_page = 'dummy'

    return req
