arr = []

n = int(input("Enter size: "))

for i in range(n):
    arr.append(int(input("Enter elements: ")))

key = int(input("Enter element to insert: "))
loc = int(input("Enter location: "))

arr.insert(loc, key)

print("Updated array:", arr)