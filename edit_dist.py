s = "h5c"
t = "h5d"

c = 0

for i in range(min(len(s), len(t))):

    if s[i] != t[i]:
        c += 1

c += abs(len(s) - len(t))

print(c)