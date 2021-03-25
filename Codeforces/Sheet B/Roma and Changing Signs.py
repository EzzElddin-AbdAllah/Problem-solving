n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] <= 0:
        a[i] *= -1
        k -= 1
    if k == 0:
        break
if k % 2 == 0:
    print(sum(a))
else:
    a[a.index(min(a))] *= -1
    print(sum(a))
