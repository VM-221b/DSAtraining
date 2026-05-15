import sys

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, ele):
        self.stack.append(ele)
        print(ele, "item pushed")

    def pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            popped = self.stack.pop()
            print(popped, "item popped")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[-1])

    def traverse(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements:")
            for item in self.stack:
                print(item)


if __name__ == '__main__':
    obj = Stack()
    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch = int(input("Make a choice: "))
        if ch == 1:
            ele = input("Enter element to push: ")
            obj.push(ele)
        elif ch == 2:
            obj.pop()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)