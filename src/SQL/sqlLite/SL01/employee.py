class ESX:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return'{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def __repr__(self) -> str:
        return 'Employee({}{}{})'.format(self.first, self.last, self.pay)

# h=ESX('parishkar','singh',1000000)
# print(h.email)