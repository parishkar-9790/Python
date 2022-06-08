# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# finding the largest element
# ...............................................................


def largest(list):
    x = 0
    for i in list:
        if i > x:
            x = i
    return x

if __name__ == '__main__':
    list = [12, 213, 234, 3, 45, 756, 67, 3323, 4]
    print("The largest number is",largest(list))
