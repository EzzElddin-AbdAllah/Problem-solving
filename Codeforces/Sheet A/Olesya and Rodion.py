a, b = map(int, input().split())
c = str(b)
d = str(a)
if len(c) == a:
    print(b)
elif len(c) > a:
    print('-1')
else:
    for i in range(len(c), a):
        b *= 10
    print(b)