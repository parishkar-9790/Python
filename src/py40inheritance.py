# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Inheritance
# ...............................................................


class empex:
    leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary}. and the role is {self.role} "

    def printd(self):
        return(self.name+" "+str(self.salary)+" "+self.role)

class programmer(empex):
    pass

if __name__ == '__main__':
    parishkar = empex("parishkar", 1000000, "engineer")
    print(parishkar.printdetails())
