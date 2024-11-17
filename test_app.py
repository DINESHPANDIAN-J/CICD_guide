from app import add_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(5, 2) == 7
    assert add_numbers(-1, 1) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 2) == 3
    assert subtract_numbers(0, 5) == -5