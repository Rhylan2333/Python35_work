#请在____处填写一行代码
#请在 … 处填写多行代码
#不要修改已给出代码
a = input()  # 请输入填充符号
c = input()  # 请输入要显示的字符串
flag = 1
while flag:
    try:
        b = eval(input())  # 请输入字符串总长度
    except:  # 如果try语句执行不成功，则执行except语句
        flag = 1
        print("请输入一个正整数")
    else:
        if type(b)== type(1) and b>0:
            flag = 0
        else:
            flag = 1
            print("请输入一个正整数")
print('{0:{1}^{2}}'.format(c,a,b))  # 新知识！嵌套的字符串格式化，用于向一个待格式化字符串引入外部变量
