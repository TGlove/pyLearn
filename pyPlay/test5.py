#-*- coding: UTF-8 -*-
print[x for x in range(10) if x%2==0]
g = lambda x:x*2
print g(2)

fs = [(lambda n , i=i : i + n) for i in range(10)]
print fs[3](4)

# nums = range(2,50)
# for i in range(2, 50):
#     nums = filter(lambda x: x == i or x % i, nums)
# print nums
