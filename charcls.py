#s=space, d=digit, w=word, 
import re
# x="\\s"
# x="\\S"
# x="\\d"
# x="\\D"
# x="\\w"
# x="\\W"
x="."
matcher=re.finditer(x,"a7b D 2@k2D8z")
for match in matcher:
    print(match.start(),'...',match.group())