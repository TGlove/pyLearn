#-*- coding: UTF-8 -*-
def calculate_fee(w,d):
    fee=0
    if w>=0 and w<=2:
        fee = 0.10*d
    elif w>2 and w<=6:
        fee = 0.12 * d
    elif w>6 and w<=10:
        fee = 0.15 * d
    elif w>10:
        fee = 0.25 * d
    else:
        print 'input is not available'
    print 'fee=',fee
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

L=range(1,101)
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

L=range(1,101)
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

#输入三个数字，从小到大排序
#冒泡排序算法
def sort_digit(a,b,c):
    temp = 0
    if a>b:
        temp=a
        a=b
        b=temp
    if b>c:
        temp=b
        b=c
        c=temp
    if a>b:
        temp=a
        a=b
        b=temp
    print a,b,c
sort_digit(-11,11,90)

print '\n\n'

L = range(1,101)
