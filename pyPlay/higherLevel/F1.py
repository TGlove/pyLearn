# -*- coding: UTF-8 -*-
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


class BStudent(BasketballMixin, Student):
    pass


class FTeacher(FootballMixin, Teacher):
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
        for k, v in kw.iteritems():
            setattr(self, k, v)


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
        return '(Student:%s,%s,%s)' % (self.name, self.gender, self.score)


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

print '\n\n'


# 斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
#
# 请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10)
# 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
class Fib(object):

    def __init__(self, num):
        L = [0, 1, 1]
        for i in range(num):
            if i > 2:
                a = L[i - 1] + L[i - 2]
                L.append(a)
        self.num = L

    def __str__(self):
        return str(self.num)

    __repr__ = __str__

    def __len__(self):
        return len(self.num)


f = Fib(10)
print f
print len(f)


#     def __str__(self):
#         return str(self.num)
#
#     __repr__ = __str__  重点 不可以忘记

# Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。
#
# 提示：
# 减法运算：__sub__
# 乘法运算：__mul__
# 除法运算：__div__

# 分数运算
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        p = self.p
        q = self.q
        if p > q:
            smallest = q
        else:
            smallest = p
        for i in range(1, smallest + 1):
            if p % i == 0 and q % i == 0:
                hsl = i
        if self.q / hsl == 1:
            return ("%s") % (self.p / hsl)
        return ("%s/%s") % (self.p / hsl, self.q / hsl)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2


# 最大公约数算法
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print gcd(5, 10)


# 请继续完善Rational，使之可以转型为float。
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / float(self.q)


print float(Rational(7, 2))
print float(Rational(1, 3))
print '\n\n'


# play private attribution
# class person():
#     __score = 0
#
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     def __str__(self):
#        return 'score : %s' % (self.__score)

# 如果没有定义set方法，就不能对“属性”赋值，这时，就可以创建一个只读“属性”。
#
# 请给Student类加一个grade属性，根据 score 计算 A（>=80）、B、C（<60）。

# 注意: 第一个score(self)是get方法，用@property装饰，第二个score(self, score)是set方法，
# 用@score.setter装饰，@score.setter是前一个@property装饰后的副产品。
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score >= 80 and self.score <= 100:
            return 'A'
        elif self.score < 80 and self.score >= 60:
            return 'B'
        elif self.score < 60 and self.score >= 0:
            return 'C'
        else:
            return 'invaild input!'


s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade

# __slots__的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存。

# 假设Person类通过__slots__定义了name和gender，请在派生类Student中通过
# __slots__继续添加score的定义，使Student类可以实现name、gender和score 3个属性。

class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('score')

    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score

print '\n\n'
# 改进一下前面定义的斐波那契数列：
#
# class Fib(object):
#     ???
# 请加一个__call__方法，让调用更简单：
#
# >>> f = Fib()
# >>> print f(10)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

class Fib(object):

    def __call__(self, num):
        L = [0, 1, 1]
        for i in range(num):
            if i > 2:
                a = L[i - 1] + L[i - 2]
                L.append(a)
        self.num = L
        return L

f = Fib()
print f(10)

# class Fib(object):
#     def __call__(self, num):
#         a, b, L = 0, 1, []
#         for n in range(num):
#             L.append(a)
#             a, b = b, a + b
#         return L
#
# f = Fib()
# print f(10)