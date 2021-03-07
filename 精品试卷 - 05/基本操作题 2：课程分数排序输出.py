# 在_____处填写一行代码
# 不得修改其他代码
# -*- coding:utf-8 -*-
studs= [{'sid':'103','Chinese': 90},{'sid':'101','Chinese': 80},{'sid':'102','Chinese': 70}]
scores = {}
k = None
for stud in studs:
    sv = stud.items()
    for it in sv:
        if it[0] =='sid':  #第一次访问：it = ('sid','103')
            k = it[1]  # k = '103'
        else:   #第二次访问：it = ('Chinese',90)，it[1] = 90
            scores[k] = it[1]  #scores["103"] = 90
so = list(scores.items())  #形如：[('103':90),('101':80),...]，一定要list()
so.sort(key = lambda x:x[0],reverse = False)
for l in so:  # so可能是list，元素是(sid, chinese)
    print('{}:{}'.format(l[0],l[1]))