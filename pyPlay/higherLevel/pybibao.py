# -*- coding: UTF-8 -*-
# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。



def calc_prod(lst):
    def g():
        a = 1
        for i in lst:
            a = a * i
        return a

    return g


b = calc_prod([1, 2, 3, 4, 5])
print b()
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1,f2,f3=count()
print f1(),f2(),f3()


def new_fn(f):
    def fn(x):
        print 'this is log,call:' + f.__name__ + '()'
        return f(x)

    return fn

@new_fn
def f1(x):
    return x * 2

print f1(5)

