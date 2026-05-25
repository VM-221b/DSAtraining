import re
count=0
# pattern=re.compile("ab")
# matcher=pattern.finditer("abaababaab")
matcher=re.finditer("ab","abaababaab")
for match in matcher:
    count+=1
    print(match.start(),' ',match.end(),' ',match.group())
print("Total no of grp occurences: ",count)