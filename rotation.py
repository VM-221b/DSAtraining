arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of rotations: "))
for i in range(k):
    last=arr[-1]
    arr=[last]+arr[:-1]
print(arr)