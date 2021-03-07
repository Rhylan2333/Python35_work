# -*- coding:utf-8 -*-
'''
This is a python123.io file.
'''
#studs列表中的元素是字典
studs= [{'sid':'103','Chinese': 90},
{'sid':'101','Chinese': 80},
{'sid':'102','Chinese': 70}]
scores = {}  
for stud in studs:
    sv = stud.items()  #sv被赋值为二维列表，形如[('sid','103'),('Chinese',90)]
    for it in sv:      
        if it[0] == 'sid':   #第一次访问：it = ('sid','103')
            k = it[1]        # k = '103'
        else:                #第二次访问：it = ('Chinese',90) it[1] = 90
            scores[k]  = it[1]   #scores["103"] = 90
so = list(scores.items())   #形如：[('103':90),('101':80),...]
so.sort(key = lambda x:x[0],reverse = False) #按学号进行排序
for l in so:
    print('{}:{}'.format(l[0],l[1]))   #遍历输出排序后结果
