n = int(input())
s = list(input())
# c = 0
# while 1:
#     if (len(s) < 2) | ('1' not in s) | ('0' not in s) | (c == len(s)-1):
#         break
#     if ((s[c] == '1') & (s[c+1] == '0')) | ((s[c] == '0') & (s[c+1] == '1')):
#         del s[c]
#         del s[c]
#         c = 0
#     else:
#         c += 1
a = s.count('1')
b = s.count('0')
print(len(s)-min(a, b)*2)
