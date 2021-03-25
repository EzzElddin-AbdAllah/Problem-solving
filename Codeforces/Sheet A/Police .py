n = int(input())
s = list(map(int, input().split()))
crime = 0
off = 0
for i in range(n):
    if s[i] == -1:
        if off == 0:
            crime += 1
        else:
            off -= 1
    else:
        off += s[i]
print(crime)