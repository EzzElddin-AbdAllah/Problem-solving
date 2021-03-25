n = int(input())
z1 = list(map(int, input().split()))
z2 = list(map(int, input().split()))
c = 0
for i in range(1, n+1):
    if (i in z1[1:]) | (i in z2[1:]):
        c += 1
if c == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")