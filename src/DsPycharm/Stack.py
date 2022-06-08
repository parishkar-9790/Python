# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Stack Complete
# ...............................................................
from collections import deque


class stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isempty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    stk = stack()
    while(1):
        choice = input(
            "enter your choice 1.push 2.pop 3.peek 4.isempty 5.size")
        if choice == '1':
            y = input("enter the value to push")
            stk.push(y)
        elif choice == '2':
            print("popped: "+stk.pop())
        elif choice == '3':
            print("The top elemet is "+stk.peek())
        elif choice == '4':
            print(stk.isempty())
        elif choice == '5':
            print(stk.size())
        elif choice == '6':
            break
