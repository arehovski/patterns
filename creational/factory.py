from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        ...

    @abstractmethod
    def calculate_perimeter(self) -> float:
        ...

    def render(self):
        print(self.__class__.__name__)
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")


class Square(Shape):
    def __init__(self, height: float):
        self.height = height

    def calculate_area(self) -> float:
        return self.height ** 2

    def calculate_perimeter(self) -> float:
        return self.height * 4


class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width

    def calculate_perimeter(self) -> float:
        return 2 * (self.height + self.width)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


def new_shape(name: str, **kwargs) -> Shape:
    if name == "circle":
        return Circle(**kwargs)
    elif name == "rect":
        return Rectangle(**kwargs)
    elif name == "square":
        return Square(**kwargs)
    else:
        raise ValueError("Unknown shape")


if __name__ == '__main__':
    shape = new_shape("circle", radius=3)
    shape.render()
    shape = new_shape("rect", height=2, width=3)
    shape.render()
    shape = new_shape("square", height=2)
    shape.render()
    shape = new_shape("lala")
