from abc import abstractmethod, ABC
from dataclasses import dataclass
from enum import Enum, auto
from typing import Iterable


class DoughWidth(Enum):
    THIN = auto()
    THICK = auto()


class DoughType(Enum):
    WHEAT = auto()
    CORN = auto()


@dataclass
class Dough:
    width: DoughWidth
    type: DoughType


class Cheese(Enum):
    MOZZARELLA = auto()
    CHEDDER = auto()


class Sauce(Enum):
    TOMATO = auto()
    PESTO = auto()


class Toppings(Enum):
    BACON = auto()
    SALAMI = auto()
    MUSHROOMS = auto()
    CHICKEN = auto()


@dataclass
class Pizza:
    dough: Dough = None
    cheese: Cheese = None
    sauce: Sauce = None
    toppings: Iterable[Toppings] = None

    def __str__(self):
        return f"{self.dough=}; {self.cheese=}; {self.sauce=}; {self.toppings=}."


class PizzaBuilder(ABC):

    @property
    @abstractmethod
    def _pizza(self): ...

    @abstractmethod
    def prepare_dough(self): ...

    @abstractmethod
    def add_cheese(self): ...

    @abstractmethod
    def add_sauce(self): ...

    @abstractmethod
    def add_toppings(self): ...

    def get_pizza(self) -> Pizza:
        return self._pizza


class MargheritaPizzaBuilder(PizzaBuilder):
    _pizza = Pizza()

    def prepare_dough(self):
        self._pizza.dough = Dough(width=DoughWidth.THICK, type=DoughType.WHEAT)

    def add_cheese(self):
        self._pizza.cheese = Cheese.MOZZARELLA

    def add_sauce(self):
        self._pizza.sauce = Sauce.TOMATO

    def add_toppings(self): ...


class ToscanaPizzaBuilder(PizzaBuilder):
    _pizza = Pizza()

    def prepare_dough(self):
        self._pizza.dough = Dough(width=DoughWidth.THIN, type=DoughType.WHEAT)

    def add_cheese(self):
        self._pizza.cheese = Cheese.CHEDDER

    def add_sauce(self):
        self._pizza.sauce = Sauce.PESTO

    def add_toppings(self):
        self._pizza.toppings = [Toppings.BACON, Toppings.MUSHROOMS]


class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_toppings()


if __name__ == '__main__':
    for builder_class in PizzaBuilder.__subclasses__():
        builder = builder_class()
        director = Director(builder)
        director.make_pizza()
        pizza = builder.get_pizza()
        print(pizza)
