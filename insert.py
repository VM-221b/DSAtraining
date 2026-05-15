arr=list(map(int, input("Enter: ").split()))
for i in range(1,len(arr)):
    current=arr[i]
    pos=i
    while current<arr[pos-1] and pos>0:
        arr[pos]=arr[pos-1]
        pos=pos-1
    arr[pos]=current
print(arr)