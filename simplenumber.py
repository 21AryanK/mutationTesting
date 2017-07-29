class SimpleNumber:

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def is_positive(self):
        if self._value >= 0:
            return True
        return False

    def increment(self, incrememter):
        if incrememter is not None:
            return incrememter.increment(self)

        return self

    # I think we can all agree this is a silly method, but here to demonstrate equivalent mutations
    def multiply_if_ones(self, otherNumber):
        if (self._value == 1 and otherNumber._value == 1):
            return SimpleNumber(self._value * otherNumber._value)

        return self
