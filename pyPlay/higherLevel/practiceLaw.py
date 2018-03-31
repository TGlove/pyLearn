#-*- coding: UTF-8 -*-

# *args  用来[解包list]将参数打包成tuple给函数体调用
# **kw   打包关键字参数成dict给函数体调用

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print calc(*nums)