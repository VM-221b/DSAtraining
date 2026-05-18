import sys

class queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front=0
        self.capacity = 5

    def isFull(self):
        if self.rear == self.capacity - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def insert(self, ele):
        if self.isFull():
            print("Overflow")
        else:
            self.queue.append(ele)
            self.rear += 1
            print(ele, "item inserted")

    def delete(self):
        if self.isEmpty():
            print("Underflow")
        else:
            popped = self.queue.pop(0)
            print(popped, "item removed")
        
    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements:")
            for item in self.queue:
                print(item)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Top element is:", self.queue[0])

if __name__ == '__main__':
    obj = queue()
    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch = int(input("Make a choice: "))
        if ch == 1:
            ele = input("Enter elements to insert: ")
            obj.insert(ele)
        elif ch == 2:
            obj.delete()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)