from calculator import hello
from calculator import hello_world


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def test_hello():
    assert hello() == "Hello world!"


def test_hello_world():
    assert hello_world() == "Hello, World!"
    assert hello_world() != hello()
