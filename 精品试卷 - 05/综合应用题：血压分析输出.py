
#在…处填写多行代码
#在_____出填写一行代码
#可以修改其他代码

jl = [[],[],[],[],[]]   # 1:zb_h, zb_l,yb_h,yb_l
zyc = []  # 左臂压差
yyc = []  # 右臂压差
with open("xueyajilu.txt", 'r',encoding='utf-8') as fi:
    for l in fi:  #对文件中的每一行内容进行处理
        if len(l):  #过滤空行
            lls = l.split(',')
            #print(l.split(','))
            #例如第一行的lls:['2018/7/2 6:00', '140', '82', '136', '90']
            #注意第一列是时间，不需要，跳过            
            for i in range(1,5):     #i从1开始，就是为了跳过第一列时间
                jl[i].append(eval(lls[i])) #构建二维列表jl
            zyc.append(eval(lls[1])- eval(lls[2]))  # 左臂高压-低压
            yyc.append(eval(lls[3])- eval(lls[4]))  # 右臂高压-低压

cnt = len(zyc)   #记录条数

res = []   #构建对比表

res.append(list(("高压最大值", max(jl[1]), max(jl[3]))))  # ["高压最大值", max_左高, max_右高]
res.append(list(("低压最大值", max(jl[2]), max(jl[4]))))
res.append(list(("压差平均值", sum(zyc)//cnt, sum(yyc)//cnt)))
res.append(list(("高压平均值", sum(jl[1])//cnt, sum(jl[3])//cnt)))
res.append(list(("低压平均值", sum(jl[2])//cnt, sum(jl[4])//cnt)))


print('{:<10}{:<10}{:<10}'.format("对比项", "左臂", "右臂"))
for r in range(len(res)):
    print('{:<10}{:<10}{:<10}'.format(res[r][0], res[r][1], res[r][2]))
