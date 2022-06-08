# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# check for triangle and compute area
# ...............................................................
import math


def checktriangle(a, b, c):
    if a >= b+c or b >= a+c or c >= a+b:
        return False
    return True


def computerarea(a, b, c):
    s = a+b+c
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


if __name__ == '__main__':
    a, b, c = map(int, input("Enter the 3 Sides : ").split())
    if checktriangle(a, b, c) :
        print("The sides represents a triangle %4.3f" % computerarea(a, b, c))
    else:
        print("Not a triangle ")
