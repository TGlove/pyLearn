# -*- coding: UTF-8 -*-
def calculate_fee(w, d):
    fee = 0
    if w >= 0 and w <= 2:
        fee = 0.10 * d
    elif w > 2 and w <= 6:
        fee = 0.12 * d
    elif w > 6 and w <= 10:
        fee = 0.15 * d
    elif w > 10:
        fee = 0.25 * d
    else:
        print 'input is not available'
    print 'fee=', fee


# w=input('weight:')
# d=input('distance:')
# calculate_fee(w,d)

# #range()函数可以创建一个数列：
#
# >>> range(1, 101)
# [1, 2, 3, ..., 100]
# 请利用切片，取出：
#
# 1. 前10个数；
# 2. 3的倍数；
# 3. 不大于50的5的倍数。

L = range(1, 101)
print L[:10]
print L[2::3]
# x=[]
# for n in L[5:51:5]:
#     x.append(n-1)
# print x
print L[4:50:5]

# 利用倒序切片对 1 - 100 的数列取出：
#
# * 最后10个数；
#
# * 最后10个5的倍数。
print '\n\n'

L = range(1, 101)
print L[-10:]
print L[-46::5]


# 字符串有个方法 upper() 可以把字符变成大写字母：
#
# >>> 'abc'.upper()
# 'ABC'
# 但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。

def firstCharUpper(str):
    return str[0].upper() + str[1:]


print firstCharUpper('abc')


# 输入三个数字，从小到大排序
# 冒泡排序算法
def sort_digit(a, b, c):
    temp = 0
    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if a > b:
        temp = a
        a = b
        b = temp
    print a, b, c


sort_digit(-11, 11, 90)

print '\n\n'

# 请用for循环迭代数列 1-100 并打印出7的倍数
L = range(1, 101)


def print_7timesNum():
    for n in L:
        if n % 7 == 0:
            print n


# print_7timesNum()

# 可见，索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素变成 (index, element)
# 这样的tuple，再迭代，就同时获得了索引和元素本身。
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for index, name in enumerate(L):
#     print index, '-', name

# zip()函数可以把两个 list 变成一个 list：
#
# >>> zip([10, 20, 30], ['A', 'B', 'C'])
# [(10, 'A'), (20, 'B'), (30, 'C')]
# 在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
#
# 提示：考虑使用zip()函数和range()函数

L = range(1, 5)
N = ['Adam', 'Lisa', 'Bart', 'Paul']
M = zip(L, N)


def print_name():
    for index, name in M:
        print index, '-', name


print_name()

# 给定一个dict：
#
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#
# 请计算所有同学的平均分。
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0  # 注意！！！！！这里要使用浮点型
for n in d.itervalues():
    sum += n
print sum / len(d)

print '\n\n'

# 请根据dict：
#
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#
# 打印出 name : score，最后再打印出平均分 average : score。

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for a, b in d.iteritems():
    sum += b
    print 'name:', a, ' ', 'score:', b
print 'average:', sum / len(d)

print '\n\n'

# 请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
#
# 提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
print [x * (x + 1) for x in range(1, 100, 2)]

print '\n\n'

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

print '\n\n'
# 在生成的表格中，对于没有及格的同学，请把分数标记为红色。
#
# 提示：红色可以用 <td style="color:red"> 实现。
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


def generate_tr(name, score):
    if score >= 60:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
    else:
        return '<tr><td >%s</td><td style="color:red">%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

print '\n\n'


# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
#
# 提示：
#
# 1. isinstance(x, str) 可以判断变量 x 是否是字符串；
#
# 2. 字符串的 upper() 方法可以返回大写的字母。
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print toUppers(['Hello', 'world', 101])

print '\n\n'

# 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
L = range(1, 10)
L2 = range(0, 10)  # 注意！！！不可以忘记101 202 等中间可以为0的数字
print [x + y * 10 + z * 100 for x in L for y in L2 for z in L if x == z]
