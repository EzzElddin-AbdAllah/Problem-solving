n = int(input())
s = input().lower()
c = 0
for i in range(26):
    if chr(97+i) in s:
        c += 1
if c == 26:
    print('YES')
else:
    print('NO')