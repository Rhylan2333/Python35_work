 #在......上一段代码
for i in range(2,1001):    #遍历[2，1000]范围上的整数,判断是否是完数。
    s = i                  #将i赋值为s 例如i = 6,s = 6
    for j in range(1,i):   # j 遍历 [1,2,3,4,5]
        if i%j == 0:       # 如果 6 % j = 0,s = s - j
            s -= j         # s = 6 - 1 - 2 - 3 ,s = 0
    if s == 0:             # 如果是s == 0, 则i 是一个完数
        print(i)           #输出i