from app import add, greet


def test_add():
    assert add(10, 20) == 30


def test_greet():
    assert greet("DevOps") == "Hello, DevOps!"
