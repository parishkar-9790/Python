# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Operator Overloading using PYTHON
# ...............................................................


class programmer:
    languages = 10

    def __init__(self, name, salary, role) -> None:
        self.name = name
        self.role = role
        self.salary = salary

    def printDetails(self):
        return f"The name of the programmer is {self.name} The salary is {self.salary} The role is {self.role}"

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(a, b):
        return 200

    def __concat__(a, b):
        return"This is returned"

    def __str__(self) -> str:
        return self.printDetails()

    def __repr__(self):
        return self.printDetails()


parishkar = programmer("parishkar", 345, 'Programmer')
emp = programmer('random emp', 85, 'cleaner')
# parishkar.printDetails()
# emp.printDetails()
print(emp)
