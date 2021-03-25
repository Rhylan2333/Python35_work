# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

#PY301-1

# -*- coding:utf-8 -*-

f = open("score.txt","r",encoding='UTF-8')
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
    sum_grade = Cal_sum_grade(D)  # 赋值
    D.append(sum_grade)  # 写入总成绩
    L.append(D)
##    D.clear()  # 清空以便下次，此步多余且致错

f.close()
L.sort(key=lambda x:x[-1],reverse=True) #按学生总成绩从大到小排序

f = open('candidate0.txt','w')
for i in range(10): #前十个学生数据写入文件中
    ls_line = L[i]
    for column in ls_line:
        f.write(str(column) + ' ')
    f.write('\n')
f.close()
