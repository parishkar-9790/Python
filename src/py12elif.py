import os 
pointer=input("Enter the value of pointer")


if pointer<2:
    print("You lost fewer points than me.")
elif pointer>2:
    print("you lost more points than me.")
else:
    print("you lost the same number of points than me.")