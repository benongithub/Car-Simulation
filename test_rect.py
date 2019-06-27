from models.rectangle import Rectangle


def test_rect():
    r = Rectangle(200, 100, 30, 20)

    assert r.e1[0] == 185
    assert r.e3[0] == 214