from simplenumber import SimpleNumber, Incrementer
from unittest import TestCase
from unittest.mock import Mock

class TestSimpleNumberIncrementer(TestCase):
    def test_no_incrementer(self):
        number = SimpleNumber(10)
        with self.assertRaises(ValueError):
            number.increment(None)

    def test_incrementer(self):
        number = SimpleNumber(1)  # Start with 1
        mock_incrementer = Mock()
        mock_incrementer.increment = Mock(return_value=1)  # Should return an integer (increment by 1)
        
        actual_incremented_number = number.increment(mock_incrementer)
        
        mock_incrementer.increment.assert_called_once_with(number)  # Ensure it was called with the correct argument
        self.assertEqual(2, actual_incremented_number.get_value())  # Check if we get the expected value

    def test_multiply_if_ones(self):
        number1 = SimpleNumber(1)
        number2 = SimpleNumber(1)
        result = number1.multiply_if_ones(number2)
        self.assertEqual(1, result.get_value())  # Should return a SimpleNumber with value 1

        number3 = SimpleNumber(2)
        result = number1.multiply_if_ones(number3)
        self.assertEqual(1, result.get_value())  # Should still return a SimpleNumber with value 1

    def test_add_if_positive(self):
        number1 = SimpleNumber(3)
        number2 = SimpleNumber(4)
        result = number1.add_if_positive(number2)
        self.assertEqual(7, result.get_value())  # Should return a SimpleNumber with value 7

        number3 = SimpleNumber(-1)
        result = number1.add_if_positive(number3)
        self.assertEqual(3, result.get_value())  # Should still return a SimpleNumber with value 3
