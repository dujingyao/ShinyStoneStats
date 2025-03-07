a = eval(input("请输入一个三位数:"))
b = a//100
s = a % 100//10
g = a % 10
print("{}的各数字之和为{}".format(a, b+s+g))