import calculator


def test_hello():
    assert calculator.hello() == "Hello world!"
    assert calculator.hello() != ""


def test_addition():
    assert calculator.addition(1, 5) == 6
    assert calculator.addition(2, 4) == 6
    assert calculator.addition(3, 3) == 6
    assert calculator.addition(4, 2) == 6
    assert calculator.addition(5, 1) == 6


def test_subtraction():
    assert calculator.subtraction(5, 1) == 4
    assert calculator.subtraction(4, 2) == 2
    assert calculator.subtraction(3, 3) == 0
    assert calculator.subtraction(2, 4) == -2
    assert calculator.subtraction(1, 5) == -4
