from simplenumber import SimpleNumber
from unittest import TestCase


class TestSimpleNumberIsPositive(TestCase):
    def test_positive(self):
        number = SimpleNumber(1)
        self.assertTrue(number.is_positive())

    def test_negative(self):
        number = SimpleNumber(-1)
        self.assertFalse(number.is_positive())

    '''
    Uncomment this test to ensure the mutation testing passes.
    It tests the boundary condition of isPositive
    '''
    #def test_boundary(self):
    #    number = SimpleNumber(0)
    #    self.assertTrue(number.is_positive())
