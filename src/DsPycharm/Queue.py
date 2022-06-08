# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Queue
# ...............................................................
from collections import deque

# Queue class


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def isempty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


# main function
if __name__ == '__main__':
    fifo = Queue()
    while(1):
        choice = input(
            "enter your choice 1.Enqueue 2.Dequeue 3.Peek 4.Isempty 5.size")
        if choice == '1':
            y = input("Enter the value to Enqueue")
            fifo.enqueue(y)
        elif choice == '2':
            print("Dequeued: "+fifo.dequeue())
        elif choice == '3':
            print("Top elemet is "+fifo.peek())
        elif choice == '4':
            print(fifo.isempty())
        elif choice == '5':
            print(fifo.size())
        elif choice == '6':
            break
