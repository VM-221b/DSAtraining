import re
str=input("Enter a str: ")
m=re.match(str,"abc@xyz_pqr")
if m is not None:
    print("Yes match available")
    print('start index: ',m.start(),'. end index:',m.end())
else:
    print("match not available")