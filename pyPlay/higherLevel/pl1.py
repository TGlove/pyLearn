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
            m = n * m
        return m

    return multip


f = calc_prod([1, 2, 3, 4])
print f()

print '\n\n'


# 闭包
def f():
    print 'f()...'

    def g():
        print 'g()...'

    return g


result = f()
result()


def calc_sum(lst):
    def lazy_sum():
        return sum(lst)

    return lazy_sum


print calc_sum(range(1, 5))()

print '\n\n'


# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
# def count():
#     fs = []
#     for i in range(1, 4):
#         print 'for start'
#
#         def f():
#             print 'function f start'
#             return i * i
#
#         print 'append start'
#         fs.append(f)
#         print 'append end'
#     return fs
#
# f1, f2, f3 = count()
# print f1(), f2(), f3()
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print f1(), f2(), f3()

print '\n\n'


# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算 f(x)=x2 时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
#
# >>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：
#
# def f(x):
#     return x * x
# 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
# myabs = lambda x: -x if x < 0 else x
# print myabs(-10)

# 利用匿名函数简化以下代码：

def is_not_empty(s):
    return s and len(s.strip()) > 0


print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])

print '\n\n'


# 装饰器 Decorator
def f1(x):
    return x * 2


def new_fn(f):
    def fn(x):
        print 'this is log,call:' + f.__name__ + '()'
        return f(x)

    return fn


g1 = new_fn(f1)
print g1(5)

# 考察一个@log的定义：
#
# def log(f):
#     def fn(x):
#         print 'call ' + f.__name__ + '()...'
#         return f(x)
#     return fn

# 但是，对于参数不是一个的函数，调用将报错

# 要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
#
# def log(f):
#     def fn(*args, **kw):
#         print 'call ' + f.__name__ + '()...'
#         return f(*args, **kw)
#     return fn
# 现在，对于任意函数，@log 都能正常工作。

# 请编写一个@performance，它可以打印出函数调用的时间。
import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)

print '\n\n'


def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)

        return wrapper

    return log_decorator


@log('DEBUG')
def test():
    pass


print test()

# 上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
import time


def performance(unit):
    def fn(f):
        def f1(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else t2 - t1
            print'call %s() in %fs %s' % (f.__name__, t, unit)
            return r

        return f1

    return fn


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)

# @decorator可以动态实现函数功能的增加，但是，经过@decorator“改造”后的函数，和原函数相比，
# 除了功能多一点外，有没有其它不同的地方？
#
# 在没有decorator的情况下，打印函数名：
#
# def f1(x):
#     pass
# print f1.__name__
# 输出： f1
#
# 有decorator的情况下，再打印函数名：
#
# def log(f):
#     def wrapper(*args, **kw):
#         print 'call...'
#         return f(*args, **kw)
#     return wrapper
# @log
# def f2(x):
#     pass
# print f2.__name__
# 输出： wrapper
#
# 可见，由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'。
# 这对于那些依赖函数名的代码就会失效。decorator还改变了函数的__doc__等其它属性。
# 如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中：
# def log(f):
#     def wrapper(*args, **kw):
#         print 'call...'
#         return f(*args, **kw)
#     wrapper.__name__ = f.__name__
#     wrapper.__doc__ = f.__doc__
#     return wrapper

# 请思考带参数的@decorator，@functools.wraps应该放置在哪：
#
# def performance(unit):
#     def perf_decorator(f):
#         def wrapper(*args, **kw):
#             ???
#         return wrapper
#     return perf_decorator
import time, functools


def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else t2 - t1
            print'call %s() in %fs %s' % (f.__name__, t, unit)
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial.__name__

print '\n\n'
# python中偏函数

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
#
# def int2(x, base=2):
#     return int(x, base)
# 这样，我们转换二进制就非常方便了：
#
# >>> int2('1000000')
# 64
# >>> int2('1010101')
# 85
# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
#
# >>> import functools
# >>> int2 = functools.partial(int, base=2)
# >>> int2('1000000')
# 64
# >>> int2('1010101')
# 85
# 所以，functools.partial可以把一个参数多的函数变成一个参数少的新函数，
# 少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。


# 我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。
# 请用functools.partial把这个复杂调用变成一个简单的函数：
#
# sorted_ignore_case(iterable)
import functools

sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2: cmp(s1.upper(),s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])