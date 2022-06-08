# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Single Inheritance
# ...............................................................

class emp:
    def __init__(self, name, cls) -> None:
        self.name = name
        self.cls = cls

    def print(self):
        print(
            f"The name of the employee is {self.name} and Semester is {self.cls}")


class programmer(emp):
    language = 10

    # def __init__(self, name, cls) -> None:
    #     super().__init__(name, cls)

    def print(self):
        super().print()
        print(f"He know {self.language} programming languages")

if __name__ == '__main__':
    parishkar=programmer("parishkar","4th Sem")
    parishkar.print()
