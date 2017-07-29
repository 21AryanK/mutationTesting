from simplenumber import SimpleNumber

def test_ones():
    number = SimpleNumber(1)
    otherNumber = SimpleNumber(1)

    newNumber = number.multiply_if_ones(otherNumber)

    assert newNumber.get_value() == 1

def test_no_ones():
    number = SimpleNumber(2)
    otherNumber = SimpleNumber(3)

    newNumber = number.multiply_if_ones(otherNumber)

    assert newNumber.get_value() == 2
    assert otherNumber.get_value() == 3

def test_only_one_one():
    number = SimpleNumber(1)
    otherNumber = SimpleNumber(2)

    newNumber = number.multiply_if_ones(otherNumber)

    assert newNumber.get_value() == 1
    assert otherNumber.get_value() == 2

    # Test the numbers the other way around
    number = SimpleNumber(2)
    otherNumber = SimpleNumber(1)

    newNumber = number.multiply_if_ones(otherNumber)

    assert newNumber.get_value() == 2
    assert otherNumber.get_value() == 1
