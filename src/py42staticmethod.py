# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# alternate constructor and split funtion
# ...............................................................

class emp:
    leaves = 8
# default constructor

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
# print the data about the class

    def print(self):
        print(
            f"The name is {self.name}. The salary is {self.salary} and the role is {self.role}.")
# class funtion to change the number of leaves

    @classmethod
    def change_leaves(cls, newleaves):
        cls.leaves = newleaves
# a alternate constructor to enter the data

    @classmethod
    def importfromstring(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

# global funtion to change the number of the leaves
    @staticmethod
    def printgood(string):
        print(f"this funtion is good and {string}")


def change(cla, leaves):
    cla.leaves = leaves


if __name__ == '__main__':
    parishkar = emp("parishkar", 1000000, "CEO")
    adam = emp("adam", 12, "to sleep")
    laptop = emp.importfromstring("Laptop-1000-machine")
    parishkar.print()
    laptop.print()
    # print(parishkar.leaves)
    # print(adam.leaves)
#   to change the class attribute permanently
    # change(emp, 10)
    # print(adam.leaves)
