val=input("enter the value you want:")
print(val)

parishkar=input("enter the value of parishkar: ")
print("the answer is ",(parishkar))
# print parishkar//pyhton 2

# type casting the inputs to the desired outcome
# num1=int(input())
# num2=int(input())
# print(num1+num2)

# taking multiple inputs
x,y,z=input("enter the value x y z:").split()
print("the value of x y z is ",x,y,z)
# print("List of students: ", x)

a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

x = list(map(int, input("Enter multiple values: ").split()))
