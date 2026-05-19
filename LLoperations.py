import sys


class getnode:

    def __init__(self):
        self.data = None
        self.next = None


class linklist:

    def __init__(self):
        self.head = None

    def append(self):

        data = int(input("Enter data: "))

        newnode = getnode()
        newnode.data = data

        if self.head == None:
            self.head = newnode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newnode

        print(data, "is added at end")

    def add_begin(self):

        data = int(input("Enter data: "))

        newnode = getnode()
        newnode.data = data

        newnode.next = self.head
        self.head = newnode

        print(data, "is added at beginning")

    def add_between(self):

        pos = int(input("Insert after which value: "))
        data = int(input("Enter new data: "))

        newnode = getnode()
        newnode.data = data

        ptr = self.head

        while ptr != None and ptr.data != pos:
            ptr = ptr.next

        if ptr == None:
            print("Value not found")

        else:
            newnode.next = ptr.next
            ptr.next = newnode

            print(data, "inserted after", pos)

    def traverse(self):

        if self.head == None:
            print("Linked List is empty")

        else:

            ptr = self.head

            while ptr != None:
                print(ptr.data, end=" -> ")
                ptr = ptr.next

            print("None")

    def delAtBeg(self):
        if self.head==None:
            print("LL not present")
        else:
            ptr=self.head
            self.head=ptr.next
            print(ptr.data, "is deleted")
    
    def delAtEnd(self):
        if self.head == None:
            print("LL not present")

    # Only one node
        elif self.head.next == None:
            print(self.head.data, "is deleted")
            self.head = None
        else:
            ptr = self.head

        while ptr.next != None:

            ptr1 = ptr
            ptr = ptr.next

        ptr1.next = None

        print(ptr.data, "is deleted")

if __name__ == '__main__':

    obj = linklist()

    while True:

        print("\n1. Append")
        print("2. Add at Beginning")
        print("3. Add in Between")
        print("4. Delete at first")
        print("5. Delete at end")
        print("6. Traverse")
        print("0. Exit")

        n = int(input("Make a choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.add_begin()

        elif n == 3:
            obj.add_between()

        elif n ==4:
            obj.delAtBeg()

        elif n==5:
            obj.delAtEnd()
        
        elif n == 6:
            obj.traverse()

        elif n == 0:
            sys.exit(0)