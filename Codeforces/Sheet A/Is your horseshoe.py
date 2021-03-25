s = list(map(int, input().split()))
a = list()
for i in s:
    if i not in a:
        a.append(i)
print(4-len(a))