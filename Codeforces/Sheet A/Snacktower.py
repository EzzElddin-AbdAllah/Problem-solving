n = int(input())
s = list(map(int, input().split()))
#d = sorted(s, reverse=True)
z = list()
# for i in range(n):
#     for j in range(n):
#         if d[i] == s[j]:
#             z.append(j)
# print(z)

for i in range(n):
    for j in range(n):
        if s[j] == max(s) - i:
            print(s[j], end=' ')
            break
        else:
            print('\n')
