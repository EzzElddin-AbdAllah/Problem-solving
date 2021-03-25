s = input()
n = 97
c = 0
for i in s:
    x = abs(ord(i) - n)
    if x > 13:
        c += abs(x-26)
    else:
        c += x
    n = ord(i)
print(c)