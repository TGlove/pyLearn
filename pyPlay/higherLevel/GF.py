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
    def __init__(self,name,gender,birth,x):


        xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

        print xiaoming.name
        print xiaoming.job