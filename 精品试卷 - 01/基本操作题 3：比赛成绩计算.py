"""
基本操作题 3：比赛成绩计算
"""

#在…处填写多行代码
#不允许修改其他代码、
score = [[87,79,90],[99,83,93],[90,75,89],[89,87,94],[95,85,84]]
for i in range(len(score)) :
    a1 = score[i][0]
    a2 = score[i][1]
    a3 = score[i][2]
    final = a1*0.6 + a2*0.3 + a3*0.1
    print('the {} final score is {}'.format(i+1, int(final)))
