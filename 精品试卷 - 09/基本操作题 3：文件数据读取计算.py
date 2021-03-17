#请在...上填写多行代码
#可以修改其他代码

fi = open("data.txt", 'r')
for l in fi:
    l = l.strip('\n').split(',')
    s = 0.0
    n = len(l)
    for i in range(n):
        item = l[i].split(':')  # 获取value数
        s += eval(item[1])
    print("总和是：{}，平均值是：{:.2f}".format(s,s/n))
fi.close()
