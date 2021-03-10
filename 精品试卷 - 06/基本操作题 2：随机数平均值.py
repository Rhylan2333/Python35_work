#在_____处填写一行代码
#不允许修改其他代码

import random
random.seed(1)
n = eval(input())
sum = 0
for i in range(n):
    fl = random.uniform(1,100)
    sum += fl
    print("{:.2f}".format(fl))
print('The average is:{:.2f}'.format(sum/n))