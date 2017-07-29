from simplenumber import SimpleNumber
from mock import Mock

def testi_no_incrementer():
    number = SimpleNumber(1)
    sameNumber = number.increment(None)
    # Uncomment this line to ensure the mutation testing passed
    #assert number == sameNumber

def testIncrementer():
    number = SimpleNumber(-1)
    expectedIncrementedNumber = SimpleNumber(2)

    mockIncrememter = Mock(return_value=expectedIncrementedNumber)

    actualIncrementedNumber = number.increment(mockIncrememter)

    mockIncrememter.increment.assert_called_once_with(number)

    # Uncomment this line to ensure the mutation testing passed
    #assert expectedIncrementedNumber == actualIncrementedNumber
