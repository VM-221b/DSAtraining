def binary_search(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            loc=mid
            break;
        elif target<arr[mid]:
            high=mid-1
        elif target>arr[mid]:
            low=mid+1

    if flag==True:
        print(f"Search successfull item {target} found at {loc}")
    else:
        print("Search unsuccessful")

if __name__ == '__main__':
    n=int(input("Enter size: "))
    arr=[]
    print(f"Enter the elements: ")
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    target=int(input("Enter the item to search: "))
    binary_search(n,arr,target)