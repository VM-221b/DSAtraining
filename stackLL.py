import sys


class GetNode:

    def __init__(self):
        self.data = None
        self.next = None


class StackLL:

    def __init__(self):
        self.head = None

    def push(self):

        data = input("Enter data: ")

        newnode = GetNode()
        newnode.data = data

        newnode.next = self.head
        self.head = newnode

        print(data, "is pushed")

    def pop(self):

        if self.head == None:
            print("Underflow")

        else:

            ptr = self.head

            self.head = ptr.next

            print(ptr.data, "is popped")

    def peek(self):

        if self.head == None:
            print("Stack is empty")

        else:
            print("Top element is:", self.head.data)

    def traverse(self):

        if self.head == None:
            print("Stack is empty")

        else:

            ptr = self.head

            print("Stack elements:")

            while ptr != None:
                print(ptr.data)
                ptr = ptr.next


if __name__ == '__main__':

    obj = StackLL()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Make a choice: "))

        if ch == 1:
            obj.push()

        elif ch == 2:
            obj.pop()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)