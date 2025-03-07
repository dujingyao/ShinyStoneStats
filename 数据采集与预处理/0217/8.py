a = input('请输入一句话：')
a += ' '
b = ''
c = []
j = 0
for i in a:
    j += 1
    if i == '.' or i == ',' or i == ' ':
        c.append(b)
        b = ''
        continue
    b += i
res = 0
for i in c:
    res += len(i)
print(res // len(c))
