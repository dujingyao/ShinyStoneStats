lst = ['python', 'programmer', 'internet', 'crawler']
num = {}
for i in lst:
    for j in i:
        if j in num:
            num[j] += 1
        else:
            num[j] = 1
print(num)