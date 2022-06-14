from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Size(Enum):
    small = "S"
    medium = "M"
    large = "L"


@dataclass
class Shoe:
    brand: str
    size: int

    def info(self):
        print(f"Shoe {self.brand=} {self.size=}")


@dataclass
class Shirt:
    brand: str
    size: Size

    def info(self):
        print(f"Shirt {self.brand=} {self.size.value=}")


class ISportsFactory(ABC):
    @abstractmethod
    def make_shoe(self, size: int) -> Shoe:
        ...

    @abstractmethod
    def make_short(self, size: Size) -> Shirt:
        ...


class AdidasFactory(ISportsFactory):
    brand = "adidas"

    def make_shoe(self, size) -> Shoe:
        return Shoe(self.brand, size=size)

    def make_short(self, size: Size) -> Shirt:
        return Shirt(self.brand, size=size)


class NikeFactory(ISportsFactory):
    brand = "nike"

    def make_shoe(self, size: int) -> Shoe:
        return Shoe(self.brand, size=size)

    def make_short(self, size: Size) -> Shirt:
        return Shirt(self.brand, size=size)


def get_sports_factory(brand: str) -> ISportsFactory:
    if brand == "nike":
        return NikeFactory()
    elif brand == "adidas":
        return AdidasFactory()
    else:
        raise ValueError("Unknown brand")


if __name__ == '__main__':
    nike = get_sports_factory("nike")
    adidas = get_sports_factory("adidas")
    nike_shoe = nike.make_shoe(size=43)
    nike_shoe.info()
    nike_shirt = nike.make_short(size=Size.large)
    nike_shirt.info()
