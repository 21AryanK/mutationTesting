import abc


class Incrementer(abc.ABC):  # pragma: no cover
    @abc.abstractmethod
    def increment(self, other_number: 'SimpleNumber'):
        raise NotImplementedError


class SimpleNumber:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def is_positive(self) -> bool:
        # Check if the value is positive or zero
        return self._value >= 0

    def increment(self, incrementer):
        if incrementer is None:
            raise ValueError("Incrementer cannot be None")

        increment_value = incrementer.increment(self)  # Get the increment value

        if not isinstance(increment_value, int):
            raise TypeError("Increment value must be an integer")

        self._value += increment_value  # Update the private attribute
        return self


    def multiply_if_ones(self, other_number: 'SimpleNumber') -> 'SimpleNumber':
        """
        Multiplies with other_number only if both values are 1.
        """
        if self._value == 1 and other_number.get_value() == 1:
            return SimpleNumber(self._value * other_number.get_value())
        return self

    def add_if_positive(self, other_number: 'SimpleNumber') -> 'SimpleNumber':
        """
        Adds other_number's value only if both values are positive.
        """
        if self.is_positive() and other_number.is_positive():
            return SimpleNumber(self._value + other_number.get_value())
        return self

