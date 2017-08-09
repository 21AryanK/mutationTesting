from simplenumber import SimpleNumber
from mock import Mock
from unittest import TestCase


class TestSimpleNumberIncrememter(TestCase):
    def test_no_incrementer(self):
        number = SimpleNumber(1)
        same_number = number.increment(None)
        # Uncomment this line to ensure the mutation testing passed
        # assert number == same_number

    def test_incrementer(self):
        number = SimpleNumber(-1)
        expected_incremented_number = SimpleNumber(2)
        mock_incrememter = Mock(return_value=expected_incremented_number)
        actual_incremented_number = number.increment(mock_incrememter)
        mock_incrememter.increment.assert_called_once_with(number)
        # Uncomment this line to ensure the mutation testing passed
        # assert expectedIncrementedNumber == actualIncrementedNumber
