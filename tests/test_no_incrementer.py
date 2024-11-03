from simplenumber import SimpleNumber
from unittest import TestCase
from unittest.mock import Mock

class TestSimpleNumberIncrementer(TestCase):
    def test_no_incrementer(self):
        number = SimpleNumber(10)
        with self.assertRaises(ValueError):
            number.increment(None)  # Testing behavior with None

        # Add more tests for invalid increment values
        invalid_incrementers = [1.5, "string", [], {}, object()]
        for inc in invalid_incrementers:
            mock_incrementer = Mock(return_value=inc)
            with self.assertRaises(TypeError):
                number.increment(mock_incrementer)

    def test_incrementer(self):
        number = SimpleNumber(-1)
        expected_incremented_number = SimpleNumber(2)
        mock_incrementer = Mock()
        mock_incrementer.increment = Mock(return_value=2)  # Should return an integer
        
        actual_incremented_number = number.increment(mock_incrementer)
        mock_incrementer.increment.assert_called_once_with(number)
        
        # Uncomment this line to ensure the mutation testing passed
        # self.assertEqual(expected_incremented_number.get_value(), actual_incremented_number.get_value())
