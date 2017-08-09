from simplenumber import SimpleNumber
from unittest import TestCase
from unittest.mock import Mock


class Object(object):
    pass


class TestSimpleNumberIncrememter(TestCase):
    def test_no_incrementer(self):
        number = SimpleNumber(1)
        same_number = number.increment(None)
        # Uncomment this line to ensure the mutation testing passed
        #self.assertEqual(number.get_value(), same_number.get_value())

    def test_incrementer(self):
        number = SimpleNumber(-1)
        expected_incremented_number = SimpleNumber(2)
        mock_incrememter = Object()
        mock_incrememter.increment = Mock(return_value=expected_incremented_number)
        actual_incremented_number = number.increment(mock_incrememter)
        mock_incrememter.increment.assert_called_once_with(number)
        # Uncomment this line to ensure the mutation testing passed
        #self.assertEqual(expected_incremented_number.get_value(), actual_incremented_number.get_value())
