# n=int(input("Enter size: "))
# print("Enter the elements: ")
# arr=[]
# for i in range(n):
#     ele=int(input("Enter element: "))
#     arr.append(ele)
# for i in range(len(arr)):
#     print(arr[i])

#SUM_OF_LIST_ELEMENTS
# n=int(input("Enter size: "))
# print("Enter the elements: ")
# arr=[]
# sum=0
# for i in range(n):
#     ele=int(input("Enter element: "))
#     arr.append(ele)

# for i in range(len(arr)):
#     sum+=arr[i]
#     print(sum)

#EVEN&ODDSUM
# if arr[i]%2==0:
# even+=arr[i]
# else odd+=arr[i]

#TOTAL_NO_OF_EVEN&ODD
#declare e1 and o1

#techNO
num = int(input("Enter the number: "))

s = str(num)

if len(s) % 2 == 0:
    mid = len(s) // 2

    n1 = int(s[:mid])
    n2 = int(s[mid:])

    total_sum = n1 + n2

    if total_sum ** 2 == num:
        print("The number is a Tech number")
    else:
        print("The number is not a Tech number")
else:
    print("The number is not a Tech number")
