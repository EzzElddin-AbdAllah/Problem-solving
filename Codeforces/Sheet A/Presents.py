n = int(input())
s = list(map(int, input().split()))
d = list()
for i in range(n):
    for j in range(n):
        if s[j] == i+1:
            d.append(j+1)
for i in range(len(d)):
    print(d[i], end=' ')
