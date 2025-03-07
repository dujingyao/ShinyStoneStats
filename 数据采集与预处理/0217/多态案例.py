class school_people:
    def say(self, who):
        who.say()
class teacher(school_people):
    def say(self):
        print('我是一名老师')
class student(school_people):
    def say(self):
        print('我是一名学生')

a = school_people()
a.say(student())
a.say(teacher())
