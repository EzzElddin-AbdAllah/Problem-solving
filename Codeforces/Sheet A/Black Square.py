n = list(map(int, input().split()))
s = input()
c = 0
for i in s:
    for x in range(1, 5):
        if int(i) == x:
            c += n[x-1]
            break
print(c)