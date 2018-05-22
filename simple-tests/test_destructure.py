from destructure import destructure


def test_simple_destructure():
    assert 1 == 1
    (name, height) = destructure(
        {'name': 'Fred', 'height': 70}, 'name', 'height')
    assert name == 'Fred'
    assert height == 70
