a, b = map(int, input().split())
i = 1
while 1:
    x = ((a*i)-b) % 10
    if (a*i) % 10 == 0:
        print(i)
        break
    if x == 0:
        print(i)
        break
    i += 1