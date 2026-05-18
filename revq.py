class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.capacity = 5

    def isFull(self):
        return self.top == self.capacity - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, ele):
        if self.isFull():
            print("Overflow")
        else:
            self.stack.append(ele)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            print("Underflow")
            return None
        else:
            popped = self.stack.pop()
            self.top -= 1
            return popped


class Queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.capacity = 5

    def isFull(self):
        return self.rear == self.capacity - 1

    def isEmpty(self):
        return self.rear == -1

    def insert(self, ele):
        if self.isFull():
            print("Overflow")
        else:
            self.queue.append(ele)
            self.rear += 1

    def delete(self):
        if self.isEmpty():
            print("Underflow")
            return None
        else:
            popped = self.queue.pop(0)
            self.rear -= 1
            return popped

    def traverse(self):
        print("Queue elements:")
        for item in self.queue:
            print(item)


# Main Program
if __name__ == '__main__':

    obj1 = Queue()
    obj2 = Stacks()

    # Insert elements into queue
    for i in range(obj1.capacity):
        ele = int(input("Enter element: "))
        obj1.insert(ele)

    print("\nOriginal Queue:")
    obj1.traverse()

    # Queue -> Stack
    for i in range(obj1.capacity):
        ele = obj1.delete()
        obj2.push(ele)

    # Stack -> Queue
    for i in range(obj2.capacity):
        ele = obj2.pop()
        obj1.insert(ele)

    print("\nReversed Queue:")
    obj1.traverse()