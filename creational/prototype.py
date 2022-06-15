import copy
from abc import ABC, abstractmethod


class IPrototype(ABC):
    @abstractmethod
    def clone(self) -> "IPrototype": ...


class Square(IPrototype):
    def __init__(self, height: float):
        self.height = height

    def clone(self) -> "Square":
        return copy.deepcopy(self)


if __name__ == '__main__':
    square = Square(height=2)
    new_square = square.clone()
    print(id(new_square) == id(square))
