arr = []

n = int(input("Enter size: "))

for i in range(n):
    arr.append(int(input("Enter elements: ")))

key = int(input("Enter element to delete: "))

found = False

for i in range(n):
    if arr[i] == key:
        found = True
        for j in range(i, n - 1):
            arr[j] = arr[j + 1]
        arr.pop()  
        print("Deleted element:", key)
        break

if not found:
    print("Element not found")

print("Array after deletion:")
print(arr)