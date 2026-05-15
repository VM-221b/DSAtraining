# def add():
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     result=a+b
#     print("Addition is ", result)

# if __name__ =='_main_':
#     add()

def add(a,b):
    res=a+b
    return res

if __name__ == '_main_':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r=add(a,b)
    print("Addition result: ",r)