n = int(input())
s = list(map(int, input().split()))
c = 1
d = 0
z = list()
for i in range(n):
    for k in range(len(s[i:n])):
        if k + i == n - 1:
            break
        if s[k+i] >= s[k + i + 1]:
            c += 1
        else:
            break
    for j in range(len(s[0:i+1])):
        if j - i == 0:
            break
        if s[i-j] >= s[i-j-1]:
            d += 1
        else:
            break
    z.append(c+d)
    c = 1
    d = 0
print(max(z))
