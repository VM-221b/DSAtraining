import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self):
        values = list(map(int, input("Enter data: ").split()))

        for data in values:
            newnode = Node(data)

            if self.root == None:
                self.root = newnode
                print(data, "inserted")
                continue

            ptr = self.root

            while True:
                if data < ptr.data:

                    if ptr.left == None:
                        ptr.left = newnode
                        break

                    ptr = ptr.left

                else:

                    if ptr.right == None:
                        ptr.right = newnode
                        break

                    ptr = ptr.right

        print(data, "inserted")

    def preorder(self):
        def pre(ptr):
            if ptr != None:
                print(ptr.data, end=" ")
                pre(ptr.left)
                pre(ptr.right)

        pre(self.root)
        print()

    def inorder(self):
        def ino(ptr):
            if ptr != None:
                ino(ptr.left)
                print(ptr.data, end=" ")
                ino(ptr.right)

        ino(self.root)
        print()

    def postorder(self):
        def post(ptr):
            if ptr != None:
                post(ptr.left)
                post(ptr.right)
                print(ptr.data, end=" ")

        post(self.root)
        print()

    def search(self):
        key = int(input("Enter key to search: "))

        def find(root, key):

            if root is None:
                return False

            if root.data == key:
                return True

            if key > root.data:
                return find(root.right, key)

            return find(root.left, key)

        if find(self.root, key):
            print(key, "found")
        else:
            print(key, "not found")

if __name__ == '__main__':
    root = BST()

    while True:
        print("\n1. Insert")
        print("2. Preorder")
        print("3. Postorder")
        print("4. Inorder")
        print("5. Search")
        print("0. Exit")

        n = int(input("Make a choice: "))

        if n == 1:
            root.insert()

        elif n == 2:
            root.preorder()

        elif n == 3:
            root.postorder()

        elif n == 4:
            root.inorder()

        elif n==5:
            root.search()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid choice")