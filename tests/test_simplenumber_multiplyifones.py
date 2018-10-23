from unittest import TestCase

from simplenumber import SimpleNumber


class TestSimpleNumberMultipleIfOnes(TestCase):
    def test_ones(self):
        number = SimpleNumber(1)
        other_number = SimpleNumber(1)
        new_number = number.multiply_if_ones(other_number)
        self.assertEqual(new_number.get_value(), 1)

    def test_no_ones(self):
        number = SimpleNumber(2)
        other_number = SimpleNumber(3)
        new_number = number.multiply_if_ones(other_number)
        self.assertEqual(new_number.get_value(), 2)
        self.assertEqual(other_number.get_value(), 3)

    def test_only_one_one(self):
        number = SimpleNumber(1)
        other_number = SimpleNumber(2)
        new_number = number.multiply_if_ones(other_number)
        self.assertEqual(new_number.get_value(), 1)
        self.assertEqual(other_number.get_value(), 2)
        # Test the numbers the other way around
        new_number = other_number.multiply_if_ones(number)
        self.assertEqual(new_number.get_value(), 2)
        self.assertEqual(other_number.get_value(), 1)
