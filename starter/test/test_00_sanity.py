import pytest

def setup_module(mod):
    from starter import settings
    mod.templating = getattr(settings, 'TEMPLATING', False)

def test_project_sanity(client):
    pass

def test_finds_templates():
    from django.template import loader
    assert loader.find_template('base.html')

def pytest_generate_tests(metafunc):
    if 'obligatory' in metafunc.funcargnames:
        metafunc.parametrize('obligatory',
                             ('ENV', 'SECRET_KEY', 'INSTANCE_URL',
                              'MEDIA_ROOT', 'STATIC_ROOT', 'INSTALLED_APPS'))

    from starter import develop, stage, live

    if 'settings' in metafunc.funcargnames:
        metafunc.parametrize('settings', (develop, stage, live))

    if 'app' in metafunc.funcargnames:
        metafunc.parametrize('app', develop.INSTALLED_APPS)

def test_obligatory(settings, obligatory):
    setting = getattr(settings, obligatory, False)
    if setting == 'T' and templating:
        pytest.skip('Skipping obligatory setting, in template mode')
    assert templating or getattr(settings, obligatory, False) != 'T'

def test_installed_apps(app):
    assert __import__(app)

def test_installation_sane(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.content == 'Starter app up'

def test_admin_sane(client):
    res = client.get('/admin/')
    assert res.status_code == 200
    dom = BeautifulSoup(res.content)
    assert (dom.findAll('h1', id='site-name')[0].text ==
            'Django administration')
