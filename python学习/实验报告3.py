# (1）编写程序，输入一个元素类型为整型的列表a,计算得到一个元组，该元组的第一个元素为列表a的最大值，其余元素为该最大值在列表中的下标。
# def find_max(a):
#     b=()
#     c=0
#     max=a[0]
#     for i in a:
#         if i>max:
#             max=i
#             x=c
#         c+=1
#     b=(max,x)
#     return b
# a=eval(input('请输入一个列表:'))
# b=find_max(a)
# print(b)
# （2）编写程序，从键盘上输入10名同学的英语成绩（百分制），分别统计出优、良、中、及格和不及格的人数。
# def check(a):
#     result=[0,0,0,0,0]
#     for i in a:
#         if 90<=i<=100:
#             result[0]+=1
#         elif 80<=i<90:
#             result[1]+=1
#         elif 70<=i<80:
#             result[2]+=1
#         elif 60<=i<70:
#             result[3]+=1
#         elif i<60:
#             result[4]+=1
#     return result
# a=eval(input('请输入一个列表，包含十个人的成绩：'))
# b=check(a)
# print('优的人数为：',b[0])
# print('良的人数为：',b[1])
# print('中的人数为：',b[2])
# print('及格的人数为：',b[3])
# print('不及格的人数为：',b[4])
# （3）编写程序，从键盘输入一个用户的18位身份证号码，从中提取出生日期并输出。
# n=input()
# j=0
# for i in n:
#     j+=1
#     if 7<=j<=14:
#         print(i,end='')
# （4）定义一个求和函数Sum(n)，该函数实现的功能是求1+2+3+…+n的和,
# 并编写主程序调用该函数，要求用户从键盘输入一个正整数m。
# def Sum(n):
#     res=0
#     for i in range(1,n+1):
#         res+=i
#     return res
# m=eval(input('请输入一个正整数:'))
# print(Sum(m))
# （5）编写一个自定义函数，用于判断一个正整数是否为素数，并利用该函数验证哥德巴赫猜想，
# 即任意大于或等于4的偶数都可以分解为两个素数之和，要求输出测试数据的所有组合。
# import math
# def check(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return 0
#     return 1
# n = eval(input('请输入一个大于4的整数:'))
# lst=[]
# for i in range(2,n+1):
#     if check(i)==1:
#         lst.append(i)
# f=0
# for i in range(4,n+1,2):
#     for x in lst:
#         for y in lst:
#             if x+y==i:
#                 print('{}测试成功:{}+{}={}'.format(i,x,y,i))
#                 f=1
#                 break
#         if f==1:
#             break
#     f=0
# （6）编写一个自定义函数，用于判断两个数是否为幸运对数。
# 所谓幸运对数是指两数相差3，且各位数字之和能被6整除的一对数，如147和150就是幸运对数。要求找出所有的3位幸运对数。
def check(x,y):
    a1=x%10
    a2=x//10%10
    a3=x//100
    b1=y%10
    b2=y//10%10
    b3=y//100
    if (a1+a2+a3+b1+b2+b3)%6==0:
        return 1
    else:
        return 0
j=1
for i in range(100,997):
    if check(i,i+3)==1:
        print('第{}对幸运数是{}和{}'.format(j,i,i+3),end=' ')
        if j%5==0:
            print()
        j+=1