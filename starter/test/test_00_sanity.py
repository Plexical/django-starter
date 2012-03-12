def test_project_sanity(client):
    pass

def test_finds_templates():
    from django.template import loader
    assert loader.find_template('base.html')
