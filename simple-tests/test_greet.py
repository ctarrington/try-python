from greet import greet


def test_greet():
    assert greet('Fred') == 'Hi there, Fred'


def test_fancy():
    assert greet('Frederick the Great') == 'Hi there, Frederick the Great'
