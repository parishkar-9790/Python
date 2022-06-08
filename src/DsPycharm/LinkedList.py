# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# linked List Complete
# ...............................................................

# defination of node


class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# defination of class and supporting methods


class linkedlist:
    def __init__(self):
        self.head = None
# insert the list into the linked list

    def insertlist(self, list):
        self.head = None
        for data in list:
            self.insertatend(data)
# insert the data in the front

    def insertathead(self, data):
        Node = node(data, self.head)
        self.head = Node
# insert the date in the end

    def insertatend(self, data):
        if self.head is None:
            self.head = node(data, None)
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = node(data, None)
# delete the given node by using index

    def deletenodebyindex(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == int(index-1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
# delete the node by data

    def deletenodebydata(self, datax):
        itr = self.head
        if itr.data == datax:
            itr = itr.next
            return
        while itr is not None:
            if itr.next.data == datax:
                itr = itr.next.next
                break
            itr = itr.next


# calculate the lenghth of the linked list


    def getLength(self):
        itr = self.head
        count = 0
        while itr is not None:
            count += 1
            itr = itr.next
        return count
# print the linked list

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr = llstr+str(itr.data) + "--->"
            itr = itr.next
        llstr = llstr+"NULL"
        print(llstr)


# the main funtion
if __name__ == '__main__':
    linked = linkedlist()
    dxr = ["parishkar", "singh", "thinks.."]
    while(1):
        x = input(
            "enter choice 1.Insert 2.InsertinEnd 3.InsertList 4.DeletebyIndex 5.DeletebyData 6.Linked list lenght 7.Print 8.break")
        if x == '1':
            y = input("enter value of add in head : ")
            linked.insertathead(y)
        elif x == '2':
            y = input("enter value to add to end : ")
            linked.insertatend(y)
        elif x == '3':
            linked.insertlist(dxr)
            print("Voila")
        elif x == '4':
            y = input("enter the index to delete : ")
            linked.deletenodebyindex(y)
        elif x == '5':
            y = input("enter the data to delete : ")
            linked.deletenodebydata(y)
        elif x == '6':
            print("The list lenght is "+linked.getLength())
        elif x == '7':
            linked.print()
        elif x == '8':
            break
