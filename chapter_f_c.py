# 随机密码生成。编写程序，在26个字母大小写和9个数字组成的列表中随机生成10个8位密码。
import random

alphabets_1 = list(chr(i) for i in range(65,91))
alphabets_2 = list(chr(i) for i in range(97,123))
nums = list(chr(i) for i in range(49,58))

ls = [alphabets_1, alphabets_2, nums]

for i in range(10) :
    for j in range(8) :
        if j < 7 :  # 0~6是七位
            print (random.choice (random.choice(ls)), end='')  # 先从ls中随机选一行random.choice(ls)，再从该行随机选一列random.choice()
            
        else :  # 7是第八位
            print(random.choice (random.choice(ls)))  # random.choice的对象可以是list
