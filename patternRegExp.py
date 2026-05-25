import re
x="[abc]"
x="[^abc]"
x="[a-z]"
x="[0-9]"
x="[a-AzA=Z0-9]"
x="[^a-zA-Z0-9]"
matcher=re.finditer(x,"a7bD2@k2$D8z")
for match in matcher:
    print(match.start(),'...',match.group())