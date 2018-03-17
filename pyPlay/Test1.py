#-*- coding: UTF-8 -*-
print '等差数列前100项求和--------'
a=1
b=0
abc=False

while abc==False:
    a=a+3
    b=b+a
    if a<100:
        abc==False
    if a>=100:
        print b
        abc=True
#多行  print 'Line 1\nLine 2\nLine 3'
print '''Line 1
Line 2
Line 3'''
# 汉字
print '''
静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''
# 整数和浮点型
1+2 # ==> 整数
1.0 + 2.0 # ==> 浮点
1 + 2.0 # ==> 浮点

# 10/4 = 2 整型只显示商 不显示余数
# 10%4 ==> 取余数 2

# 布尔型

#与
# True and True ==> True
# True and False ==> False
# False and True ==> False
# False and False ==> False

#或
# True or True ==> True
# True or False ==> True
# False or True ==> True
# False or False ==> False

# not True   # ==> False
# not False   # ==> True

a = True
print a and 'a=T' or 'a=F'

# True and 'a=T' 计算结果是 'a=T'
# 继续计算 'a=T' or 'a=F' 计算结果还是 'a=T'

#List
List = ['David','123','456','Trancy']
print List

empty_list = []
print empty_list

L = [95.5, 85, 59]
print L[0],L[1]
# print L[3]
print '-------'
print L[-1],L[-2],L[-3]
# print L[-4]
print '-------'
L.append('new added thing')
print L
L.insert(0,'first added')
print L
L.insert(2,'between 95.5&85')
print L
print '----------------- \n'

Delete = L.pop(2)
print L,'\n',Delete

L[0] = 'First was insteaded'
print L

#元组 tuple 不可更改
t = ('Adam', 'Lisa', 'Bart')
print '元组',t[2]
t1 = (1,)
print t1

t = ('a', 'b', ['A', 'B'])

L = t[2]
L[0] = 'X'
L[1] = 'Y'
print t,'\n\n'

#if -----------
age = 1
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >=6:
    print 'U R teenager'
elif age >=3:
    print 'U R kid'
else:
    print 'U R baby'
print 'END'

print '\n\n'

#for -----------
L = [75, 92, 59, 68]
for name in L:
    print name

print '\n\n'

#while ---------

#100以内奇数和
sum = 0
x = 1
while x<100:
    sum +=x
    x = x+2
print sum

#利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum = 0
x = 1
n = 1
while True:
    sum += x
    x = 2*x
    n = n+1
    if n > 20:
        break
print 'sum=',sum

#continue --------------------
#对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print sum

#多重循环 -----------------
#对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [ 1,2,3,4,5,6,7,8,9,]:
    for y in [ 1,2,3,4,5,6,7,8,9]:
        if x<y:
            print x*10 + y
