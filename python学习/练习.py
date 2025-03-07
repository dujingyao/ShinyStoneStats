# 1
# class Vehicle:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def describe(self):
#         return f"这辆车的品牌是{self.model}，这辆车的颜色是{self.color}。"
# class Car(Vehicle):
#     def __init__(self, model, color, number_of_door):
#         super().__init__(model, color)
#         self.number_of_door = number_of_door
#
#     def describe(self):
#         base_describe = super().describe()
#         return f"{base_describe}该车的车门数是{self.number_of_door}"
#
#
# class Motorcycle(Vehicle):
#     def __init__(self, model, color, engine_size):
#         super().__init__(model, color)
#         self.engine_size = engine_size
#
#     def describe(self):
#         base_describe = super().describe()
#         return f"{base_describe}该车的发动机数是{self.engine_size}"
#
#
# # 测试
# car = Car("宝马", "白色", "4")
# motor = Motorcycle("奔驰", "黑色", "5")
# print(car.describe())
# print(motor.describe())


# class Vehicle:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#     def describe(self):
#         return f"This is a {self.color} {self.model}."
# class Car(Vehicle):  #定义子类，继承Vehicle类
#     def __init__(self, model, color, number_of_doors):
#         super().__init__(model, color)             # 调用父类的构造方法
#         self.number_of_doors = number_of_doors  # 定义子类的属性
#     def describe(self):        # 重写父类的方法
#         base_description = super().describe()  # 调用父类的方法并把结果赋值给base_description
#         return f"{base_description} It has {self.number_of_doors} doors."
# class Motorcycle(Vehicle):  #定义子类，继承Vehicle类
#     def __init__(self, model, color, engine_size):
#         super().__init__(model, color)         # 调用父类的构造方法
#         self.engine_size = engine_size       # 定义子类的属性
#     def describe(self):
#         base_description = su
#         per().describe() # 调用父类的方法并把结果赋值给base_description
#         return f"{base_description} It has a {self.engine_size} cc engine."
# # 测试代码
# car = Car("Toyota Camry", "Blue", 4)
# print(car.describe())
#
# motorcycle = Motorcycle("Harley-Davidson", "Black", 1200)
# print(motorcycle.describe())
# 2
# class LibraryBook:
#     def __init__(self, title, author, isbn, borrowed=False):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.borrowed = borrowed
#     def borrow_book(self):
#         if not self.borrowed:   # 如果没有被借出
#             self.borrowed = True
#             print(f"书籍{self.title}已成功借出。")
#         else:
#             print(f"书籍{self.title}已被借出。")
#     def return_book(self):
#         if self.borrowed:
#             self.borrowed = False
#             print("书籍‘{self.title}’已成功归还。")
#         else:
#             print("书籍‘{self.title}'未被借出。")
#     def check_status(self):
#         status = '已借出' if self.borrowed else '在馆'
#         print(f"书籍‘{self.title}’的借阅状态为：{status}")
# book = LibraryBook("python编程","张三","12345")
# while True:
#     print("\n请选择操作：")
#     print("1.借阅书籍")
#     print("2.归还书籍")
#     print("3.查询书籍借阅状态")
#     print("4.退出")
#     choice = input("请输入选项(1/2/3/4):")
#     if choice == '1':
#         book.borrow_book()
#     elif choice == '2':
#         book.return_book()
#     elif choice == '3':
#         book.check_status()
#     elif choice == '4':
#         print("感谢使用图书馆系统，再见！")
#         break;
#     else:
#         print("无效选择，请重新输入！")
# 3
# str = input('请输入一段话：')
# string = {}
# char = ''
# for i in str:
#     char = char + i
#     if i == ' ':
#         string[char] = 0
# for i in string.keys():
#     string[i] += 1
# max = 0
# max_char = ''
# while len(string):
#     for i, j in string.values(), string.keys():
#         if i >= max:
#             max_char = j
#             max = i
#     print(j, end=' ')
#     string.pop(j)
#     max = 0
# 正确版案例三
# from jieba import *
# from jieba.analyse import *
# text = input('请输入一段话:')
# word_dict = {}
# words = lcut(text)   # 返回分词后的结果列表
# for word in words:
#     if len(word) == 1:
#         continue
#     else:
#         word_dict[word] = word_dict.get(word, 0)+1   # 如果word这个键存在，则返回这个键所对应的值，否则返回默认值，即0
# sort_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)    # lambda是一个匿名函数，代表以x这列表或者元组的第二个元素来排序，即x[1]
# for word, count in sort_list:
#     print(f'{word:^10}{count:>10}')
# 案例四
# def check(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return True
#     return False
# sum = 0
# for i in range(1,101):
#     if check(i)==False:
#         print(i, end=' ')
#         sum+=1
# print()
# print(sum)
# 案例五
# n = eval(input('请输入一个整数：'))
# lst = []
# lst.append(1)
# lst.append(1)
# for i in range(2, n):
#     lst.append(lst[i-2]+lst[i-1])
# print(lst)
# 案例六
# id = input('请输入用户名')

# 另一个练习集
# 根据身份证号输出出生日期案例
# import re
# number = input('请输入身份证号:')
# match = re.search(r'(\d{4})(\d{2})(\d{2})', number[6:14])
# if match:
#     year, month, day = match.groups()
# print(f"出生日期为{year}年{month}月{day}日")

# 判断回文数
# text = input('请输入:')
# res = text[::-1]
# if res==text:
#     print('YES')
# else:
#     print('NO')

# 简单指法练习：系统随机输出一条语句，由用户输入，计算用户输入的准确率。
# import random
# import string
# sentences = [
#     "The quick brown fox jumps over the lazy dog.",
#     "The rain in Spain falls mainly on the plain.",
#     "Type this sentence without any mistakes.",
#     "Hello, World!",
#     "Python is fun to learn."
# ]
# # 随机去选择一条语句
# def choose_sentencce():
#     return random.choice(sentences)
# 计算用户输入的准确性
# def user_accuracy(user_input,correct_sentence):
#     # 将句子分割成单词列表，并去除空字符串
#     correct_words = [word for word in correct_sentence.split() if word]  # 句子的单词数
#     print(correct_words)
#     user_words = [word for word in user_input.split() if word]   # 用户输入的单词数
#     print(user_words)
#     # 计算匹配的单词数量
#     # 遍历correct_word,如果word也在user_words里出现，那么加一
#     correct_count = sum(1 for word in correct_words if word in user_words)
#     # 计算准确率
#     accuracy = correct_count/len(correct_words)
#     return accuracy
# correct_sentence = choose_sentencce()
# print('请输入下面的句子:')
# print(correct_sentence)
# # 用户输入
# user_input = input('请输入：')
# accuracy = user_accuracy(user_input,correct_sentence)
# print("您的准确率是： {:.2f}%".format(accuracy * 100))

# import string
#
# with open("yy06.txt", 'w', encoding='utf-8') as file:
#     file.write("学到了很多")

# 99乘法表
# with open("9981.txt", 'w', encoding='UTF-8') as file:
#     for i in range(1, 10):
#         for j in range(1, i+1):
#             file.write(f"{j}*{i}={i*j}\t")
#         file.write('\n')

# works = input('请输入一段话：')
# count_work = {}
# lst = works.split()
# lst2 = list(set(lst))
# for i in lst2:
#     num = works.count(i)
#     count_work[i] = num
# sorted(count_work, reverse=True)
# print(count_work)