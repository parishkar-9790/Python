# stack 1 left to right
# stack 2 right to left

class doubleStack:
    capacity = 0
    list = []
    Top1 = 0
    Top2 = 0

    def __init__(self, size):
        self.capacity = size
        self.Top1 = -1
        self.Top2 = size
        self.list = [None]*size

    def push(self, stackType, data):
        if stackType == 1 and (self.Top1+1) < self.Top2:
            self.Top1 += 1
            self.list[self.Top1] = data
        elif stackType == 2 and (self.Top2-1) > self.Top1:
            self.Top2 -= 1
            self.list[self.Top2] = data
        else:
            print('DoubleStack Overflow')

    def pop(self, stackType):
        if stackType == 1 and self.Top1 > -1:
            self.list[self.Top1] = None
            self.Top1 -= 1
        elif stackType == 2 and self.Top2 < self.capacity:
            self.list[self.Top2] = None
            self.Top2 += 1
        else:
            print('Stack Underflow')

    def isStackEmpty(self):
        return not any(self.list)

    def isStackFull(self):
        return any(self.list)

    def printStack(self):
        for i in self.list:
            print(i, end='   ')
        print()

    def visualizeStack(self):
        for i, val in enumerate(self.list):
            if i == self.Top1:
                print('Top1->', val, end='   ')
            elif i == self.Top2:
                print(val, '<-Top2', end='   ')
            else:
                print(val, end='   ')
        print()


if __name__ == '__main__':
    x = int(input('Enter the Size of the DoubleStack-> '))
    stack = doubleStack(x)
    n = 1
    while True:
        print('Active Stack->', n)
        x = input(
            'Choose: 1.Push  2.Pop  3.isEmpty  4.isFull  5.Print List  6.VisualizeStack 7.Swap Stack ---> ')
        if x == '1':
            data = input(f'Enter data to Push in Stack {n}-> ')
            stack.push(n, data)
        elif x == '2':
            stack.pop(n)
        elif x == '3':
            print('Stack Empty:', stack.isStackEmpty())
        elif x == '4':
            print('Stack Full:', stack.isStackFull())
        elif x == '5':
            stack.printStack()
        elif x == '6':
            stack.visualizeStack()
        elif x == '7':
            n = n == 2 and 1 or 2
