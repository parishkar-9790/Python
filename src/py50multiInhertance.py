# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Multiple Inheritance
# ...............................................................

class emp:
    def __init__(self, name, cls, role) -> None:
        self.name = name
        self.cls = cls
        self.role = role

    def printEMP(self):
        print(
            f'The name of the employee is {self.name} and Semester is {self.cls} and role is {self.role}')


class programmer(emp):
    language = 10

    # def __init__(self, name, cls) -> None:
    #     super().__init__(name, cls)

    def printProgrammer(self):
        super().print()
        print(f'He know {self.language} programming languages')


class player:
    no_of_games = 4

    def __init__(self, name, game) -> None:
        self.name = name
        self.game = game

    def printPlayer(self):
        print(f'The name is {self.name} and the game is {self.game}')


class coolProgrammer(emp, player):
    var = 10
    language = "C++"

    def printLanguage(self):
        print(self.language)


if __name__ == '__main__':
    parishkar = coolProgrammer('parishkar', '4th Sem', 'c++')
    print(parishkar.no_of_games)
