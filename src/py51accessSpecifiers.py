# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# access specifiers
# ...............................................................

# from typing_extensions import Self


class emp:
    leaves = 10
    var = 10
    _protec = 200
    __private = 400

    def printDetails(self):
        print(
            f"The number of leaves{self.leaves} the var is {self.var} and the protected value is {self._protec} and the private is {self.__private}")


parishkar = emp()
parishkar.printDetails()
parishkar._emp__private = 20
print(parishkar._emp__private)
