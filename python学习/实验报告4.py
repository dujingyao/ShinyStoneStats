# 设计一个简单的学生信息管理系统，学生信息包括学号、姓名、年龄、性别、专业、学院等。要求实现以下功能：
# （1）学生信息录入功能；
# （2）学生信息浏览功能；
# （3）学生信息查询功能，按学号、姓名查询；
# （4）学生信息的删除与修改。
class Member:       # 定义基类
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
class Student(Member):     # 定义学生子类
    def __init__(self,id,name,sex,age,major,department):
        Member.__init__(self, name, sex, age)
        self.id=id
        self.major = major
        self.department = department
        print('学生信息已录入成功！')
# 浏览学生信息
def look(lst):
    j=1
    for i in lst:
        print('第{}个学生的学号为：'.format(j),i.id,end=' ')
        print('第{}个学生的姓名为：'.format(j), i.name,end=' ')
        print('第{}个学生的性别为：'.format(j), i.sex,end=' ')
        print('第{}个学生的年龄为：'.format(j), i.age,end=' ')
        print('第{}个学生的专业为：'.format(j), i.major,end=' ')
        print('第{}个学生的学院为：'.format(j), i.department)
        j+=1
# 学生信息查询
def query(lst,id1,name1):
    for i in lst:
        if i.id==id1 and i.name==name1:
            print('查询成功！')
            print('该学生的学号为：', i.id, end='  ')
            print('该学生的姓名为：', i.name, end='  ')
            print('该学生的性别为：', i.sex, end='  ')
            print('该学生的年龄为：', i.age, end='  ')
            print('该学生的专业为：', i.major, end='  ')
            print('该学生的学院为：', i.department)
            return
    print('查询失败!')
# 学生信息删除和修改
def delete(lst,id1,name1):
    j=0
    for i in lst:
        if i.id==id1 and i.name==name1:
            del lst[j]
            print('删除成功！')
            return
        j+=1
    print('删除失败！')
def modify_id(lst,before,after):
    j=0
    for i in lst:
        if i.id==before:
            lst[j].id=after
            return
        j+=1
def modify_name(lst,before,after):
    j=0
    for i in lst:
        if i.id==before:
            lst[j].name=after
        j+=1
def modify_sex(lst,before,after):
    j=0
    for i in lst:
        if i.id==before:
            lst[j].sex=after
        j+=1
def modify_age(lst,before,after):
    j=0
    for i in lst:
        if i.id==before:
            lst[j].age=after
        j+=1
def modify_major(lst,before,after):
    j=0
    for i in lst:
        if i.id==before:
            lst[j].major=after
        j+=1
def modify_department(lst,before,after):
    j=0
    for i in lst:
        if i.id==before:
            lst[j].department=after
        j+=1
# 录入学生信息(主函数）
students=[]
n = eval(input('请输入学生的个数：'))
for i in range(1,n+1):
    id = input('请输入第{}个学生的学号：'.format(i))
    name = input('请输入第{}个学生的姓名：'.format(i))
    sex = input('请输入第{}个学生的性别：'.format(i))
    age = input('请输入第{}个学生的年龄：'.format(i))
    major = input('请输入第{}个学生的专业：'.format(i))
    department = input('请输入第{}个学生的学院：'.format(i))
    student = Student(id,name,sex,age,major,department)
    students.append(student)
opr = eval(input('请选择要进行的操作：浏览学生信息请输入1，查询请输入2，删除请输入3，修改请输入4:'))
if opr == 1:
    look(students)
if opr == 2:
    id = input('请输入要查询学生的学号：')
    name = input('请输入要查询学生的姓名：')
    query(students,id,name)
if opr == 3:
    id = input('请输入要删除学生的学号：')
    name = input('请输入删除学生的姓名：')
    delete(students,id,name)
if opr == 4:
    m = eval(input('请输入要修改几项:'))
    for i in range(1,m+1):
        x = input('请输入要修改的第{}项：'.format(i))
        id = input('请输入该生的学号：')
        if x=='学号':
            after = input('请输入修改后的学号：')
            modify_id(students,id,after)
        if x=='姓名':
            after = input('请输入修改后的姓名：')
            modify_name(students, id, after)
        if x=='性别':
            after = input('请输入修改后的性别：')
            modify_sex(students, id, after)
        if x=='年龄':
            after = input('请输入修改后的年龄：')
            modify_age(students, id, after)
        if x=='专业':
            after = input('请输入修改后的专业：')
            modify_major(students, id, after)
        if x=='学院':
            after = input('请输入修改后的学院：')
            modify_department(students, id, after)
if opr == 3 or opr == 4:
    print('操作成功！以下是操作后的学生名单：')
    look(students)
