n, k = map(int, input().split())
s = list(map(int, input().split()))
#z = dict()
for i in range(1, n):
    s[i] += s[i - 1]
    #z.append(z[i-1] + s[i])
b = 0
t = s[k-1]
for i in range(k, n):
    if t > (s[i]-s[i-k]):
        t = s[i] - s[i-k]
        b = i
if b == 0:
    print(1)
else:
    print(b + 2 - k)






# if n == k:
#     print(1)
#     exit()
# y = sum(s[0:k])
# for i in range(n-k):
#     y = y - s[i] + s[i+k]
#     #z[i] = sum(s[i:i+k])
#     if y < b:
#         b = y
#         j = i
# print(j+1)
# x = min(z.values())
# for i in range(len(s)):
#     if z[i] == x:
#         print(i+1)
#         exit()
