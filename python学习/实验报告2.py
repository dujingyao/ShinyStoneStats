# （1）编程产生三个0~100之间的随机整数a、b和c，将三个整数从小到大的顺序进行排序输出。
# import random
# a = random.randint(0, 100)
# b = random.randint(0, 100)
# c = random.randint(0, 100)
# numbers = [a, b, c]
# numbers.sort()
# for i in range(0, 3):
#     print(numbers[i], end=' ')
# （2）编写程序，接收用户通过键盘输入的1~13的整数，将其转换成扑克牌张输出，
#     1转换为字符’A’，2~9转换为对应的字符，10转换为字符’T’，11转换为字符’J’，
#     12转换为字符’Q’，13转换为字符’K’。要求使用if语句实现。
x = input('请输入1~13的整数:')
if('0'<x<='1'):
    x = 'A'
elif('2'<=x<='9'):
    x = x
elif(x == '10'):
    x = 'T'
if(x == '11'):
    x = 'J'
elif(x == '12'):
    x = 'Q'
elif( x== '13'):
    x = 'K'
print(x)
# （3）编写程序，接收用户输入的年份和月份，输出该月天数。要求使用if语句实现。
# year = eval(input('请输入年份:'))
# month = eval(input('请输入月份:'))
# if(year%400 == 0 or year%100 != 0 and year%4 == 0):
#     day2 = 28
# else:
#     day2=29
# if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#     day = 31
# elif(month == 2):
#     day=day2
# else:
#     day = 30
# print('{}年{}月的天数为{}'.format(year, month, day))
# （4）编写程序，输入整数n（n≥0），使用循环语句求n!。
# n = eval(input('请输入一个整数:'))
# sum = 1
# for i in range(1,n+1):
#     sum*=i
# print('{}!为:{}'.format(n,sum))
# （5）一个球从100m高度自由落下，每次落地后反弹回原高度的一半，再落下，再反弹。
# 求它在第10次落地时，共经过多少米，第10次反弹多高。
# high = 100
# sum1 = 100
# for i in range(9):
#     high/=2
#     sum1+=high*2
# print("十次共反弹的和:",sum1)
# print("第十次反弹的高度:",high)

# （6）输出所有满足以下条件的3位整数：该数是素数，该数的个位和十位数之和被10除，
# 所得余数正好就是该数的百位数。例如293是素数并且(3+9)被10除的余数是2，所以293是满足条件的3位数整数。
# import math
# def is_prime(n):
#     if n <= 1:
#         return 0
#     for i in range(2, int(math.sqrt(n)) + 1):  # 只需检查到sqrt(n)
#         if n % i == 0:
#             return 0
#     return 1
# for i in range(100, 1000):
#     if is_prime(i):
#         a = i % 10
#         b = i//10 % 10
#         c = i//100
#         if c == (a+b) % 10:
#             print(i, end=' ')
