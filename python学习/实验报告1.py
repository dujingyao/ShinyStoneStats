#(1)
'''
a = eval(input('请输入一个数字:'))
print(a//100)
'''
#(2)
'''
r = eval(input('请输入半径:'))
import math
print('周长为:{},面积为:{}'.format(2*math.pi*r,math.pi*r*r))
'''
#(3)
'''
a = eval(input('C语言成绩:'))
b = eval(input('Java语言成绩:'))
c = eval(input('Python语言成绩:'))
print('评均成绩为:{:.1f}'.format((a+b+c)/3))a
'''
#(4)
'''
s = [9,7,8,3,2,1,55,6]
print('元素之和为:',sum(s))
print('元素个数为:',len(s))
print('元素最小值为:',min(s))
print('元素最大值为:',max(s))
'''
#(5)
'''
a = input('输入一个大写字母:')
b = a.lower()
print('该字母的小写为:',b)
'''
#(6)
x=eval(input('请输入一个三位数:'))
a=x//100
b=x//10%10
c=x%10
d=c*100+b*10+a*1
print('该数的逆袭为:{},该数的数字之和为{}'.format(d,a+b+c))