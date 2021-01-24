# 对用户输入的数字进行“类型判断”，输出“浮点数”or“整数”
num = eval(input('请输入一个数字：'))
if type(num) == type(111) :
    print("输入的数字是整数。")
elif type(num) == type(1.11) :
    print("输入的数字是浮点数。")

else :
    print("这条信息不会显示，书给的代码功能不对")
