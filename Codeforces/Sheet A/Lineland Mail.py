n = int(input())
s = list(map(int, input().split()))
print(abs(s[0]-s[1]), abs(s[0]-s[n-1]))
mn = abs(s[0]-s[n-1])
mx = 0
for i in range(1, n-1):
    if abs(s[i] - s[i-1]) < abs(s[i] - s[i+1]):
        mn = abs(s[i] - s[i-1])
    else:
        mn = abs(s[i] - s[i+1])
    if abs(s[i] - s[0]) > abs(s[i] - s[n-1]):
        mx = abs(s[i] - s[0])
    else:
        mx = abs(s[i] - s[n-1])
    print(mn, mx)
    mn = abs(s[0] - s[n - 1])
    mx = 0
print(abs(s[n-1]-s[n-2]), abs(s[n-1]-s[0]))