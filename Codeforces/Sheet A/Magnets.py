n = int(input())
m = list()
c = 1
for i in range(n):
    m.append(list(map(int, input().split())))
for i in range(n-1):
    if m[i] != m[i+1]:
        c = c + 1
print(c)
