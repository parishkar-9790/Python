# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Multiple Exception Demo
# ...............................................................

import math


if __name__ == '__main__':
    while True:
        x = input(
            'Choose Exception To Throw 1.Name Error  2. Type Error  3.Value Error  4.File Not Found Error  5.Index Error  6.Division Error ')
        try:
            if x == '1':
                print(hey)
            elif x == '2':
                Int = 100
                Str = "10"
                myResult = Int/Str
            elif x == '3':
                print(math.sqrt(-1))
            elif x == '4':
                f = open('D:\\C++\\Python\\src\\parishkar2.txt')
            elif x == '5':
                list = []
                print(list[10])
            elif x == '6':
                print(10/0)

        except (NameError, FileNotFoundError, ValueError, TypeError, IndexError, ZeroDivisionError) as e:
            print(e)
