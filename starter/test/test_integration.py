from BeautifulSoup import BeautifulSoup

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
