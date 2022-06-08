# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# method overiding
# ...............................................................
class A:
    classString = "I am a String of class A"

    def __init__(self) -> None:
        self.constring = "I am inside the constructor of class A"
        self.classString = "I am a string of class A"


class B(A):
    classString = "I am a string of Class B"

    # def __init__(self) -> None:
    # super().__init__()
    def __init__(self) -> None:
        super().__init__()
        self.classString = "i am inside the contructor of class B"


a = A()
b = B()
print(b.classString)
