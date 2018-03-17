#-*- coding: UTF-8 -*-
# dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print len(d)
print 'Lisa:', d.get('Lisa') # d['Lisa']
#insert & update
d['Paul'] = 72
print d
for key in d:
    print key,d.get(key)

#set ------------
#set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的
#set存储的元素和dict的key类似，必须是不变对象
s = set(['A', 'B', 'C', 'C'])
print s,'A' in s

weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = '???' # 用户输入的字符串
if x in weekdays:
    print 'input ok'
else:
    print 'input error'

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0],':',x[1]


print '\n\n'
#add
s = set([1, 2, 3])
s.add(4)
print s
#remove
#用add()可以直接添加，而remove()前需要判断。
if 4 in s:
    s.remove(4)
print s

print '\n\n'

#time ------------------
import time;

ticks = time.time()
localtime1 = time.localtime(time.time())
localtime2 = time.asctime(time.localtime(time.time()))
print "当前时间戳为:", ticks
print "本地时间为 :", localtime1
print "本地格式化时间为 :", localtime2

print'\n\n'

# 格式化成2016-03-20 11:45:39形式
print '格式化成2016-03-20 11:45:39形式:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print '格式化成Sat Mar 28 22:24:24 2016形式:',time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print '将格式字符串转换为时间戳:',time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

print'\n\n'

import calendar

cal = calendar.month(2018, 3)
print "以下输出2016年1月份的日历:"
print cal;


# 函数 -------------------
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

print abs(-1)
print cmp(1,1)
print int('123')
print str(1234)
print '''\n\n'''
