# -*- coding: UTF-8 -*-
# class Person:
#     age = 0
#     pass
#
#
# xiaoming = Person()
# xiaohong = Person()
#
# print xiaoming
# print xiaohong
# print xiaoming == xiaohong

# 请创建包含两个 Person 类的实例的 list，并给两个实例的 name 赋值，然后按照 name 进行排序。
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,lambda x,y:cmp(x.name,y.name))

print L2[0].name
print L2[1].name
print L2[2].name

# 请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，
# 还可接受任意关键字参数，并把他们都作为属性赋值给实例。

class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# 给Person类的__init__方法中添加name和score参数，并把score绑定到__score属性上，看看外部是否能访问到。
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
try:

    print p.__score

except:

    print 'attributeerror'

# 请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，
# 这样就可以统计出一共创建了多少个 Person 的实例。
class Person:
    count = 0
    def __init__(self, name):
        Person.count = Person.count + 1
        self.name = name
p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

