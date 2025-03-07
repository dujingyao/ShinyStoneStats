class Stu:
    def __init__(self, c, python, java):
        self.c = c
        self.python = python
        self.java = java

    def p(self):
        print((self.c + self.python + self.java) // 3)
        if self.java < 60 or self.c < 60 or self.python < 60:
            print('no')
        else:
            print('yes')
st1 = Stu(100,60,50)
st1.p()