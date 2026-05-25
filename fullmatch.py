import re
str=input("Enter a str: ")
m=re.fullmatch(str,"abcabcabc")
if m is not None:
    print("Yes match available")
else:
    print("match not available")