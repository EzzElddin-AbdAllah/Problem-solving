s = list(input().lower())
for j in range(s.count('a')):
    s.remove('a')
for j in range(s.count('o')):
    s.remove('o')
for j in range(s.count('y')):
    s.remove('y')
for j in range(s.count('u')):
    s.remove('u')
for j in range(s.count('i')):
    s.remove('i')
for j in range(s.count('e')):
    s.remove('e')
for j in s:
    print('.'+j,end='')