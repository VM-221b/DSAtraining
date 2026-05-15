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

def rev_array(arr):
    stack = []
    
    for ele in arr:
        stack.append(ele)
    
    for i in range(len(arr)):
        arr[i] = stack.pop()
    
    return arr


if __name__ == '__main__':
    obj = Stack()
    arr = [234235, 235, 647]
    print("Original array:", arr)
    reversed_arr = rev_array(arr)
    print("Reversed array:", reversed_arr)