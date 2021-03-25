n = input()
s = list()
for i in n:
    if i not in s:
        s.append(i)
if len(s) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
