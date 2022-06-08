class emp:
    leaves = 6

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}"


parishkar = emp()
hehe = emp()

parishkar.name = "parishkar"
parishkar.salary = 5000000
hehe.name = "hehe"
hehe.salary = 1000
print(parishkar.printdetails())
