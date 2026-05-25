import sys

class Graph:  
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.nodeCount = 0

    def addNode(self, v):
        if v in self.nodes:
            print(f"{v} is already present")
        else:
            self.nodeCount += 1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp = [0] * self.nodeCount  
            self.graph.append(temp)
            print(f"{v} is added")

    def addEdg_Undirect_Nweigh(self, v1, v2):
        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = 1
        self.graph[index2][index1] = 1
        print(f"Edge added between {v1} and {v2}")

    def addEdg_Undirect_Weigh(self, v1, v2, weight):
        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = weight
        self.graph[index2][index1] = weight
        print(f"Weighted edge ({weight}) added between {v1} and {v2}")

    def addEdg_Direct_Weigh(self, v1, v2, weight):
        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = weight
        print(f"Directed edge ({weight}) added from {v1} -> {v2}")

    def display(self):  
        if self.nodeCount == 0:
            print("Graph is empty")
            return
        print("\nNodes:", self.nodes)
        for row in self.graph:
            print(" ".join(map(str, row)))  

    def delete(self, v):
        if v not in self.nodes:
            print(f"{v} is not present in the graph")
            return

        index = self.nodes.index(v)
        self.nodes.remove(v)
        self.nodeCount -= 1
        
        self.graph.pop(index)
        
        for row in self.graph:
            row.pop(index)
            
        print(f"{v} has been successfully deleted")


if __name__ == '__main__':
    obj = Graph()
    while True:
        print("\n1. (Insertion) add a node using adjacency matrix representation")
        print("2. (Insertion) add an edge using adjacency matrix representation")
        print("3. (Insertion) add an edge to undirected weighted graph")
        print("4. (Insertion) add an edge to directed weighted graph")
        print("5. Print graph")
        print("6. Delete operation")
        print("0. Exit\n")
        
        try:
            n = int(input("Enter any choice: "))
        except ValueError:
            print("Please enter a valid integer choice.")
            continue
        
        if n == 1:
            v = input("Enter vertex: ")
            obj.addNode(v)
        elif n == 2:
            v1 = input("Enter v1: ")
            v2 = input("Enter v2: ")
            obj.addEdg_Undirect_Nweigh(v1, v2)
        elif n == 3:
            v1 = input("Enter v1: ")
            v2 = input("Enter v2: ")
            try:
                weight = int(input("Enter weight: "))
                obj.addEdg_Undirect_Weigh(v1, v2, weight)
            except ValueError:
                print("Invalid input for weight.")
        elif n == 4:
            v1 = input("Enter source (v1): ")
            v2 = input("Enter destination (v2): ")
            try:
                weight = int(input("Enter weight: "))
                obj.addEdg_Direct_Weigh(v1, v2, weight)
            except ValueError:
                print("Invalid input for weight.")
        elif n == 5:
            obj.display()
        elif n == 6:
            v = input("Enter vertex to delete: ")
            obj.delete(v)
        elif n == 0:
            sys.exit(0)
        else:
            print("Invalid choice! Try again.")