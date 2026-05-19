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

        print(data, "is added")

    def traverse(self):

        if self.head == None:
            print("Linked List is empty")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, end=" -> ")
                ptr = ptr.next

            print("None")


if __name__ == '__main__':

    obj = linklist()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("0. Exit")

        n = int(input("Make a choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 0:
            sys.exit(0)