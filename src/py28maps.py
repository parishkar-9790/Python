
number = ["3", "34", "65"]
# using number to conver list of strings into number
for i in range(len(number)):
    number[i] = int(number[i])
# using map 
number = list(map(int, number))
number[2] = number[2]+1
# print the coverted number
print(number[2])


def sq(a):
    return a*a


# using maps to throw edited objects
num = [2, 3, 4, 5, 7, 8, 4]
square = list(map(sq, num))
print(square)

# using lambda funtion to change the values


def square(a):
    return a*a


def cube(a):
    return a*a*a


func2 = [square, cube]
for i in range(5):
    val=list(map(lambda x:x(i),func2))
    print(val)