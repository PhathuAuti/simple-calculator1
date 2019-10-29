import calculator

def test_add():
    assert calculator.add(0, 0) == 0

def test_add_negative_numbers():
    assert calculator.add(-1, -1) == -2

def test_add_digits():
    assert calculator.add(4, 5) == 9

def test_add_more():
    assert calculator.add(1,2,3,4) == 10

def test_multiply_digits():
    assert calculator.multiply(1, 2) == 2

def test_multiply_more():
    assert calculator.multiply(1,2,3,4) == 24
