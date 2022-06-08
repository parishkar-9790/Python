
def add(a, b):
    return a+b


def minus(x, y): return x-y


print(minus(1, 2))


def myfunc(n):
    return lambda a: a*n

trip=myfunc(3)
print(trip(4))