import calculator

def test_add_zeroes():
    assert calculator.add(0, 0) == 0

def test_add_two_negative_numbers():
    assert calculator.add(-1, -1) == -2

def test_add_two_positive_numbers():
    assert calculator.add(4, 5) == 9

def test_add_many_integers():
    assert calculator.add(1,2,3,4) == 10

def test_multiply_two_integers():
    assert calculator.multiply(1, 2) == 2

def test_multiply_many_integers():
    assert calculator.multiply(1,2,3,4) == 24
