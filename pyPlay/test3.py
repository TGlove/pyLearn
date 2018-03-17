#-*- coding: UTF-8 -*-
#sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100
n =0
list = []
while n<100:
    n = n+1
    list.append(n*n)
print sum(list)

#请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和
def square_of_sum(list):
    a=0
    for n in list:
            a = n*n + a
    return a
list1 = [1,2,3,4,5,6]
print square_of_sum(list1)

# 一元二次方程的定义是：ax² + bx + c = 0
# 请编写一个函数，返回一元二次方程的两个解。
# 注意：Python的math包提供了sqrt()函数用于计算平方根。
import math
def get_result_of_eqavelent(a,b,c):
    if b*b - 4*a*c >= 0:
        return (-b + math.sqrt(b*b-4*a*c))/2*a , (-b - math.sqrt(b*b-4*a*c))/2*a
    else:
        return '无解'

print get_result_of_eqavelent(1,2,3)

# 我们来计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示,
# 所以，fact(n)可以表示为 n * fact(n-1)，只有n=1时需要特殊处理。
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n
print fact(7)

# 汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
# 我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
# 如果a只有一个圆盘，可以直接移动到c；
# 如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
# 请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
# move(n, a, b, c)
# 例如，输入 move(2, 'A', 'B', 'C')，打印出：
# A --> B
# A --> C
# B --> C
def move(n, a, b, c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

def greet(name='world'):
    print 'Hello, ' + name + '.'
greet()
greet('Bart')

#请编写接受可变参数的 average() 函数。
def average(*args):
    sum=0
    for a in args:
        sum = a + sum
    return sum/len(args)
print average(1,2,3)

#SEND + MORE = MONEY 都是十进制求三个数字
# PALE
def sepJudgeValue(_val, _list, _num):  # 将数值分成元组并判断元组中是否有相同数字
    for x in range((_num - 1), -1, -1):
        _list.append(_val / (10 ** x) % 10)
    for y in range(0, _num):
        for z in range(0, _num):
            if y == z:
                continue
            else:
                if _list[y] == _list[z]:
                    return False
    else:
        return True


def comValue(_sList, _mList):  # 判断两元组之间的关系
    for x in range(0, 4):
        for y in range(0, 4):
            if x == 1 and y == 3:
                if _sList[1] != _mList[3]:
                    return False
            else:
                if _sList[x] == _mList[y]:
                    return False
    else:
        return True

    # 主程序过程


for _SEND in range(8000, 10000):  # M为进位，显然可知M=1
    sendList = []
    if sepJudgeValue(_SEND, sendList, 4):
        for _MORE in range(1000, 2000):
            moreList = []
            if sepJudgeValue(_MORE, moreList, 4):
                if (comValue(sendList, moreList)):
                    _MONEY = _SEND + _MORE
                    moneyList = []
                    _money = moreList[0] * (10 ** 3) + moreList[1] * (10 ** 2) + sendList[2] * 10 + sendList[1]
                    if (_MONEY / 10) == _money and sepJudgeValue(_MONEY, moneyList, 5):
                        print "SEND:%d,MORE:%d,MONEY:%d" % (_SEND, _MORE, _MONEY)

