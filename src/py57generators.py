# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# generators 
# ...............................................................
def gen(n):
    for i in range(n):
        yield i
        
def fibonacci(n):
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
        
def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
        yield fact

for i in gen(5):
    print(i,end=' ')
print()
for i in factorial(5):
    print(i,end=' ')
print()
for i in fibonacci(10):
    print(i,end=' ')
print()

p='parishkar'
ier=iter(p)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())