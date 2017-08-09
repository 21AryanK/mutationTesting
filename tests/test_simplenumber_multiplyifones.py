from simplenumber import SimpleNumber


def test_ones():
    number = SimpleNumber(1)
    other_number = SimpleNumber(1)
    new_number = number.multiply_if_ones(other_number)
    assert new_number.get_value() == 1


def test_no_ones():
    number = SimpleNumber(2)
    other_number = SimpleNumber(3)
    new_number = number.multiply_if_ones(other_number)
    assert new_number.get_value() == 2
    assert other_number.get_value() == 3


def test_only_one_one():
    number = SimpleNumber(1)
    other_number = SimpleNumber(2)
    new_number = number.multiply_if_ones(other_number)
    assert new_number.get_value() == 1
    assert other_number.get_value() == 2
    # Test the numbers the other way around
    number = SimpleNumber(2)
    other_number = SimpleNumber(1)
    new_number = number.multiply_if_ones(other_number)
    assert new_number.get_value() == 2
    assert other_number.get_value() == 1
