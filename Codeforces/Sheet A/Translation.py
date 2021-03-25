s1 = list(input())
s2 = list(input())
temp = list()
for i in range(len(s1)):
    temp.append(s1[len(s1)-1-i])
if s2 == temp:
    print('YES')
else:
    print('NO')