s = input()
a = input()
ans = 0
for i in range(len(a)):
    if a[i] == s[ans]:
        ans += 1
print(ans + 1)
