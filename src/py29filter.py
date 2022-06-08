# -----------------------------------------filter-----------------

from functools import reduce
list_1 = {1, 23, 4, 5, 6, 7, 45, 457, 34}


def isGreater(num):
    return num > 5


greaterthan5 = list(filter(isGreater, list_1))
print(greaterthan5)
# ----------------------------------reduce---------------------

list2 = [1, 2, 3, 4]
num = 0
for i in list2:
    num = num+i
print(num)

prod = reduce(lambda x, y: y+x, list2)
print(prod)
