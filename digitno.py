import re
number=input("Enter mobile no: ")
match=re.fullmatch("[6-9]\\d{9}",number)
if match!=None:
    print(number,"is valid mobile no")
else:
    print(number,"is not valid mobile no")