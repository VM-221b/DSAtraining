arr=list(map(float, input("Enter the values: ").split()))
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]: #change sign for descending order
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
selectionsort(arr)
print(arr)