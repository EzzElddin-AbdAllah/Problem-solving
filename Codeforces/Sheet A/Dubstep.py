s = list(input().split('WUB'))
for i in range(len(s)):
    if s[i] == '':
        continue
    print(s[i], end=' ')
# while 1:
#     if (s[i] == 'W') & ('U' in s) & ('B' in s):
#         s.remove('W')
#         s.remove('U')
#         s.remove('B')
#     else:
#         break
# print(s)