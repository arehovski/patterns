from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def draw(self): ...


class Line(Graphic):
    def draw(self):
        print('Line')


class Rectangle(Graphic):
    def draw(self):
        print('Rectangle')


class Text(Graphic):
    def draw(self):
        print('Text')


class Picture(Graphic):
    def __init__(self):
        self._children: List[Graphic] = []

    def draw(self):
        print('Picture')
        for obj in self._children:
            obj.draw()

    def add(self, obj: Graphic):
        if obj not in self._children:
            self._children.append(obj)

    def remove(self, obj: Graphic):
        self._children.remove(obj)

    def get_child(self, index):
        return self._children[index]


if __name__ == '__main__':
    pic = Picture()
    pic.add(Line())
    pic.add(Rectangle())
    pic.add(Text())

    pic2 = Picture()
    pic2.add(Text())
    pic.add(pic2)
    pic.draw()
    print("-----------")
    pic.remove(pic2)
    pic.draw()
