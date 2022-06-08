# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Abstract CLass
# ...............................................................
from abc import ABCMeta, abstractmethod

class shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
    
class rectangle(shape):
    type = "rectangle"
    side = 4

    def __init__(self) -> None:
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return f'lenght is {self.length} breadth is {self.breadth} area is {self.length*self.breadth}'


rect = rectangle()
print(rect.printarea())
