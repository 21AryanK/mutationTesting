from unittest import TestCase
from simplenumber import SimpleNumber

class TestSimpleNumberIsPositive(TestCase):
    def test_positive(self):
        number = SimpleNumber(1)
        self.assertTrue(number.is_positive())

    def test_negative(self):
        number = SimpleNumber(-1)
        self.assertFalse(number.is_positive())

    def test_boundary(self):
        number = SimpleNumber(0)
        self.assertTrue(number.is_positive())  # 0 is considered non-negative
