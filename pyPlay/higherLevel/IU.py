# -*- coding: UTF-8 -*-
import types


class Person():
    def __init__(self, name, score, **kw):
        self.name = name
        self.score = score
        for n, v in kw.iteritems():
            setattr(self, n, v)


def fn_get_score(sco):
    if sco > 80:
        return 'A'
    elif sco > 60 and sco <= 79:
        return 'B'
    return 'C'


p1 = Person('BOb', 79)
p1.get_grade = types.MethodType(fn_get_score, p1, Person)
print p1.get_grade()


# 由于属性可以是普通的值对象，如 str，int 等，也可以是方法，还可以是函数，
# 大家看看下面代码的运行结果，请想一想 p1.get_grade 为什么是函数而不是方法：
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'


p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()


# 如果将类属性 count 改为私有属性__count，则外部无法读取__score，
# 但可以通过一个类方法获取，请编写类方法获得__count值。
class Person(object):
    __count = 0

    @classmethod
    def how_many(self):
        return self.__count

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1


print Person.how_many()

p1 = Person('Bob')

print Person.how_many()


class Student(Person):
    def __init__(self, name, score, gender):
        super(Student.self).__init__(name)
        self.score = score
        self.gender = gender


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course

print '\n\n'


# 请根据继承链的类型转换，
# 依次思考 t 是否是 Person，Student，Teacher，object 类型，并使用isinstance()判断来验证您的答案
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)

print '\n\n'


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name


def who_am_i(x):
    print x.whoAmI()


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)
# 这是动态语言和静态语言（例如Java）最大的差别之一。
# 动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。

# Python提供了open()函数来打开一个磁盘文件，并返回 File 对象。File对象有一个read()方法可以读取文件内容：
#
# 例如，从文件读取内容并解析为JSON结果：
# import json
# f = open('/path/to/file.json', 'r')
# print json.load(f)

# 由于Python的动态特性，json.load()并不一定要从一个File对象读取内容。
# 任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。
#
# 请尝试编写一个File-like Object，把一个字符串 r'["Tim", "Bob", "Alice"]'包装成 File-like Object
# 并由 json.load() 解析。
print('\n\n')
import json

f = open('C://Users/chengcheng/Desktop/test.txt', 'r')
lines = f.readline()
# for line in lines:
#     print line
while(lines):
    print lines

    lines = f.readline()
f.closed

