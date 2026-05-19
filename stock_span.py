N = 7
price = [100, 80, 60, 70, 60, 75, 85]

ans = [1]

for i in range(1, N):
    if price[i] < price[i-1]:
        ans.append(1)
    else:
        ans.append(2)

for i in range(N):
    print(ans[i]**3)