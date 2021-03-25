# -*- coding:utf-8 -*-
# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

'''
输入文件 ： candidate0.txt
输出文件 ： candidate.txt
'''


f = open("candidate0.txt","r")
# ,encoding='UTF-8'
D = [] #单个学生的数据
L = [] #所有学生原始成绩和总成绩。L是矩阵



def Cal_sum_grade(D):
    '''计算单个学生总成绩'''
    sum_grade = 0
    for grade in D[2:]:
        sum_grade += int(grade)
    return sum_grade



'''读取学生单科成绩并计算总成绩'''
lines = f.readlines()
for line in lines:
    D = line.split()  # 读取单个学生的数据
    L.append(D)
##    D.clear()  # 清空以便下次，此步多余且致错

f.close()
L.sort(key=lambda x:x[-1],reverse=True) #按学生总成绩从大到小排序


'''现在L是排序好的矩阵了'''
f = open('candidate.txt','w')
for line in L:
    for grade in line[2:-1]:
        if int(grade) < 60:
            break
    else:
        f.write(line[0]+line[1]+'\n')
f.close() 
