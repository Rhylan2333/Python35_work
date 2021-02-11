# 用random库生成一个包含10个0~100之间随机数的列表
import random

ls = []
c = 1
while c <= 10 :
    num = random.randint(0,100)  # int不可迭代
    ls.append(num)
    c += 1

print(ls)
