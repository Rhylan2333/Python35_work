#-*- coding:utf-8 -*-
#在 _____上补充一行代码 
#在…….上补充多行代码

n = input()
nums = n.split(',') 
s = 0
for i in nums:
    s += eval(i)
print(s)