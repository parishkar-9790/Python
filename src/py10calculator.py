from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
z=x/y
print(z)
print(f'''"the value in with more precision digits 
is {z:.500f}"''')
