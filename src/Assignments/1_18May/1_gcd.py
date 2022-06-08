# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# GCD of two numbers using Euclid method
# ...............................................................

def GCD(x, y):
    if x == 0 and y == 0:
        return False
        # raise Exception("Error, both numbers are zero")
    if x == 0:
        return y
    if y == 0:
        return x
    if x == y:
        return y
    if x > y:
        return GCD(x-y, y)
    return GCD(x, y-x)

    # main
if __name__ == '__main__':
    a, b = map(int, input("Enter two numbers x and y: ").split())
    if GCD(a, b):
        print("GCD of both numbers is ", GCD(a, b))
    else:
        print("Error both numbers are zero")
