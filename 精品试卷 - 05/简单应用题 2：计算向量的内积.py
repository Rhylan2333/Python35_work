#在________处填写一行代码
#在....处填写多行代码
#允许修改其他代码

flag = 1
while flag:
    try:
        n = eval(input())
        xin = input().split(',')
        yin = input().split(',')
        z = zip(xin,yin)
        sum = 0
        for x,y in z:
            sum += int(x)*int(y)
        flag = False
        print("x和y的内积是:", sum)
    except:
       print("请输入整数！")
       flag = 1
