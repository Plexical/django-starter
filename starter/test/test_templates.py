from starter.test.support import render_raw

def test_base_sanity():
    assert '<!-- marker -->' in render_raw('base.html', marker='marker')
