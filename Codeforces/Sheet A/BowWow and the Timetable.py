# sb = list(input())
# sd = 0
# c = 1
# for i in reversed(range(len(sb))):
#     sd += int(sb[len(sb)-i-1]) * pow(2, i)
# while sd > 4:
#     sd = sd // 4
#     c += 1
# print(c)


sb = list(input())
if len(sb) == 1:
    print('0')
    exit()
sd = 0
c = 0
sb.reverse()
for i in range(len(sb)):
    sd += int(sb[i]) * pow(2, i)
for i in range(1, sd+1):
    c += 1
    if pow(4, i) >= sd:
        break
print(c)
