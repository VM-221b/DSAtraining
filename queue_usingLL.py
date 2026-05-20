class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def delete(self):
        if self.front is None:
            print("Queue Underflow")
            return None

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def peek_front(self):
        return self.front.data if self.front else "Queue is empty"

    def peek_rear(self):
        return self.rear.data if self.rear else "Queue is empty"

    def traverse(self):
        current = self.front
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) if elements else "Queue is empty")

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

q.traverse()

print("Deleted:", q.delete())

q.traverse()

print("Front:", q.peek_front())
print("Rear:", q.peek_rear())