
from unittest import result


def func(food):
    for x in food:
        print(x)


fruits = ["parishkar", "singh", "rajawat"]
func(fruits)

# function return values


def my_function(x):
    return 5 * x


# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# def name(args):
#     pass

# to recurse in python


# def parishkar(k):
#     if(k > 0):
#         result = k+parishkar(k-1)

#     else:
#         result = 0
#     print(result)
#     return result


# parishkar(4)

# sort function using lambda


def a_first(a):
    return a[1]


a = [[1, 14], [10, 6], [8, 23]]
a.sort(key=lambda x: x[1])
print(a)
