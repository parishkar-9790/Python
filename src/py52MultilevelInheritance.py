# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Multilevel Inheritance
# ...............................................................
class dad:
    basketball = 1


class son(dad):
    dance = 10
    basketball=12
    def isDance(self):
        print(f"Yes i can dance {self.dance} no of times")


class grandson(son):
    basketball=10
    dance = 20

    def isDance(self):
        print(f"I dance faster {self.dance}")


darry = dad()
larry = son()
harry = grandson()
print(harry.basketball)
