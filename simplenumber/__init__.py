import abc


class Incrementer(abc.ABC):  # pragma: no cover
    @abc.abstractmethod
    def increment(self, other_number: 'SimpleNumber'):
        raise NotImplementedError


class SimpleNumber:
    def __init__(self, value: int = 0):
        self._value = value

    def get_value(self) -> bool:
        return self._value

    def is_positive(self) -> bool:
        if self._value >= 0:
            return True
        return False

    def increment(self, incrememter: Incrementer) -> 'SimpleNumber':
        if incrememter is not None:
            return incrememter.increment(self)
        return self

    def multiply_if_ones(self, other_number: 'SimpleNumber') -> 'SimpleNumber':
        """
        I think we can all agree this is a silly method, but here to demonstrate equivalent mutations
        """
        if self._value == 1 and other_number.get_value() == 1:
            return SimpleNumber(self._value * other_number.get_value())
        return self
