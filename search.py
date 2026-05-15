def ls(n,arr,target):
    flag=False
    loc=-1

    for i in range(n):
        if arr[i]==target:
            flag=True
            loc=i
            print(f"search successful for item {target}, found at {loc}")
            break

    if not flag:
        print("search unsuccessful")
            
if __name__ == '__main__':
    n=int(input("Enter size: "))
    arr=[]
    print(f"Enter the elements: ")
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    target=int(input("Enter the item to search: "))
    ls(n,arr,target)