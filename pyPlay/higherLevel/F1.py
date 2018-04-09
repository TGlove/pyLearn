#-*- coding: UTF-8 -*-
# +-Person
#   +- Student
#   +- Teacher
#
# 是一类继承树；
#
# +- SkillMixin
#    +- BasketballMixin
#    +- FootballMixin
#
# 是一类继承树。
#
# 通过多重继承，请定义“会打篮球的学生”和“会踢足球的老师”。
class Person(object):
    pass

class Student(Person):
    def indentify(self):
        return 'I am a student'

class Teacher(Person):
    def indentify(self):
        return 'I am a teacher'

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin,Student):
    pass

class FTeacher(FootballMixin,Teacher):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()

# 对于Person类的定义：
#
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# 希望除了 name和gender 外，可以提供任意额外的关键字参数，并绑定到实例，
# 请修改 Person 的 __init__()定 义，完成该功能。
class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gerder = gender
        for k,v in kw.iteritems():
            setattr(self,k,v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course


print('\n\n')

# 请给Student 类定义__str__和__repr__方法，使得能打印出<Student: name, gender, score>：
#
# class Student(Person):
#     def __init__(self, name, gender, score):
#         super(Student, self).__init__(name, gender)
#         self.score = score
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student:%s,%s,%s)'%(self.name,self.gender,self.score)

s = Student('Bob', 'male', 88)
print s

# def compare(a,b,c):
#     temp = 0
#     if a>b:
#         temp = a
#         a = b
#         b = temp
#     if b>c:
#         temp = b
#         b = c
#         c = temp
#     if a>b:
#         temp = a
#         a = b
#         b = temp
#     print a,b,c
# while(1):
#     a, b, c = input('please input three number :')
#     compare(a, b, c)

# In Python 2, __cmp__(self, other) implemented comparison between two objects,
# returning a negative value if self < other, positive if self > other, and zero if they were equal.

# 请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score > s.score:
            return -1
        elif self.score < s.score:
            return 1
        else:
            if self.name > s.name:
                return 1
            elif self.name < s.name:
                return -2
            else:
                return 0

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)

