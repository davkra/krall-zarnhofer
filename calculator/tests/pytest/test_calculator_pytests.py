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


def test_multiplication():
    assert calculator.multiplication(1, 5) == 5
    assert calculator.multiplication(2, 4) == 8
    assert calculator.multiplication(3, 3) == 9
    assert calculator.multiplication(4, 2) == 8
    assert calculator.multiplication(5, 1) == 5


def test_division():
    assert calculator.division(5, 1) == 5
    assert calculator.division(4, 1) == 4
    assert calculator.division(3, 1) == 3
    assert calculator.division(2, 1) == 2
    assert calculator.division(1, 1) == 1
