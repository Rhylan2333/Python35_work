#程序读入一个表示星期几的数字（1-7），输出对应的星期字符串名称。例如，输入3，返回“星期三”。
msg = input("读入一个表示星期几的数字（1-7），我将输出对应的星期字符串名称：\n")
i = eval(msg)
weeks=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
if 1<= i < 8 :
    print("对应 " + weeks[i-1] + "。")
else :
    print("你说 " + msg + " 对应星期几？？？")
