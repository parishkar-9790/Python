# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# termwork 4
# ...............................................................

class person:
    def __init__(self, firstname, lastname, email):
        self.fname = firstname
        self.lname = lastname
        self.email = email

    @property
    def fullname():
        return fname + " " + lname
    
    def show(self):
        return self.fname + " " + self.lname + " " + self.email + " "


class customer(person):
    def __init__(self, firstname, lastname, email, no):
        super().__init__(firstname, lastname, email)
        self.custno = no

    def show(self):
        return str(super().show()) + self.custno + " "


class employee(person):
    def __init__(self, firstname, lastname, email, pan):
        super().__init__(firstname, lastname, email)
        self.pan = pan

    def show(self):
        return str(super().show()) + self.pan + " "


def isInstance(obj):
    if (obj.__class__.__name__ == 'customer'):
        return "This is a customer object"
    elif (obj.__class__.__name__ == 'employee'):
        return "This is a employee object"


if __name__ == '__main__':
    while (True):
        x = input("Enter you choice 1.Customer 2.Employee 3.Instance-> ")
        if x == '1':
            temp = input("firstname/lastname/email/no-> ")
            cust = customer(*temp.split('/'))
            print(cust.show())
            print(isInstance(cust))
        elif x == '2':
            temp = input("firstname/lastname/email/pan-> ").split('/')
            emp = employee(*temp.split('/'))
            print(emp.show())
            print(isInstance(emp))
