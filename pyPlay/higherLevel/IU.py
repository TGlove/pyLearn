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
    def __init__(self,name):
        self.name = name
        Person.__count = Person.__count + 1

print Person.how_many()

p1 = Person('Bob')

print Person.how_many()