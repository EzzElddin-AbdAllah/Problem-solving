n = int(input())
c = 0
s = map(int, input().split())
print(max(s))


# s = [0]
# s += list(map(int, input().split()))
# c = 0
# for i in range(n, 0, -1):
#     c += (s[i] - s[i-1])
# print(c)