# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Setter and Property Decorators
# ...............................................................


class emp:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@gmail.com'

    def explain(self):
        return f'This employee is {self.fname} {self.lname}'

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return f'{self.fname}.{self.lname}@gmail.com'

    @email.setter
    def email(self, string):
        names = string.split('@')[0]
        self.fname, self.lname = names.split('.')[0], names.split('.')[1]
        # self.lname=names.split('.')[0]

    @email.deleter
    def email(self):
        self.fname, self.lname = None, None


parishkar_singh = emp('parishkar', 'singh')
# asus_tuf = emp('asus', 'tuf')
parishkar_singh.email = "parishkar.work@gmail.com"
del parishkar_singh.email
print(parishkar_singh.email)
