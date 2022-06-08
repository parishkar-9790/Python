try:
    x = int(input("x: "))
except ValueError:
    print("this is not a int")
    exit()

try:
        y = int(input("y: "))
except ValueError:
    print("this is not an int!")
    exit()
print(x + y)
