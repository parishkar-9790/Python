# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# args and kwargs
# ...............................................................

from pip import main


def funtion_name(a, b):
    print(a, b)


def funargs(*args, **kwargs):
    print(type(args))
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)


# funtion_name("parishkar", "singh")

if __name__ == '__main__':
    name = ["keyboard", "mouse", "laptop", "light", "tv"]
    dict = {"hindi": "english", "device": "laptop", "games": "forza"}
    funargs(*name, **dict)
