# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Converting numbers to words in python
# ...............................................................

# https://pypi.org/project/inflect/
import inflect


def convertDigits(a):
    return inflect.engine().number_to_words(a)


if __name__ == '__main__':
    a = int(input("Enter the Number you want to Convert: "))
    print(convertDigits(a))
