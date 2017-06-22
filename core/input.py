from abc import ABC, abstractmethod


class Input(ABC):
    @abstractmethod
    def value(self):
        pass


class InputStr(Input):
    def __init__(self, msg):
        self._msg = msg

    def value(self) -> str:
        return input(self._msg + '\n')


class InputFloat(Input):
    def __init__(self, msg):
        self._str_input = InputStr(msg)

    def value(self) -> float:
        return float(self._str_input.value())


class YesInput(Input):
    def __init__(self):
        self._str_input = InputStr("Do you want to add one more triangle? (y/n)")

    def value(self) -> str:
        return self._str_input.value().lower().strip()
