
ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)
# print(ls)
# list comprehensions
list2 = [i for i in range(100) if i % 3 == 0]
# print(list2)
# dict comprehensions
dict = {i: f'item{i}' for i in range(10)}
# print(dict)

evens = (i for i in range(100) if i % 2 == 0)
for i in evens:
    print(i, end=' ')
# print(evens)
