s = list(input().lstrip('{').rstrip('}').split(', '))
if s == ['']:
    print('0')
    exit()
d = list()
for i in s:
    if i not in d:
        d.append(i)
print(len(d))
