n, f = map(int, input().split())
s = [[int(j) for j in input().split()] for i in range(n)]
c = 0
a = 0
x2 = []
x1 = list()
for i in range(n):
    x2.append(min(s[i][0]*2, s[i][1]) - min(s[i][0], s[i][1]))
x2.sort(reverse=True)
#x2 = sorted(x2.items(), key=lambda kv: kv[1], reverse=True)
for i in range(n):
    c += min(s[i][0], s[i][1])
    if a != f:
        c += x2[i]
        a += 1
# for i in range(f):
#     c += x2[i][0]
#     x1.append(x2[i][1])
# for i in range(n):
#     if i in x1:
#         continue
#     else:
#         c += min(s[i][0], s[i][1])
print(c)
# for i in range(n):
#     if (min(s[i][0], s[i][1]) < min((s[i][0]*2), s[i][1])) & (c != f):
#         s[i][0] *= 2
#         c += 1
#     a += min(s[i][0], s[i][1])
# print(a)