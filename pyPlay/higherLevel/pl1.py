# -*- coding: UTF-8 -*-
# ---函数式编程---
import math


def add(x, y, f):
    return f(x) + f(y)


print add(25, 9, math.sqrt)


# ---map()---
# 假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，
# 把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
#
# 输入：['adam', 'LISA', 'barT']
# 输出：['Adam', 'Lisa', 'Bart']
def utter_a(x):
    return x.capitalize()


print map(utter_a, ['adam', 'LISA', 'barT'])


# ---reduce()---
# Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
#
# 输入：[2, 4, 5, 7, 12]
# 输出：2*4*5*7*12的结果
def multiply_a(x, y):
    return x * y


print reduce(multiply_a, [2, 4, 5, 7, 12])


# ---filter()---
# filter()函数是 Python 内置的另一个有用的高阶函数，
# filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()
# 据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
# 注意: s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。

# 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
#
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def operate(x):
    return True == math.sqrt(x).is_integer()


print filter(operate, range(1, 101))


# python中自定义排序函数
# 但 sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，
# 传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，
# 如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
# sorted()也可以对字符串进行排序，字符串默认按照ASCII大小来比较

# 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
#
# 输入：['bob', 'about', 'Zoo', 'Credit']
# 输出：['about', 'bob', 'Credit', 'Zoo']
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    else:
        return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

print '\n\n'


# ---python中返回函数---
def f():
    print 'call f()...'

    # 定义函数g:
    def g():
        print 'call g()...'

    # 返回函数g:
    return g


x = f()
print x
x()
print '\n\n'
# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def multip():
        m = 1
        for n in lst:
            m = n*m
        return m
    return multip

f = calc_prod([1, 2, 3, 4])
print f()