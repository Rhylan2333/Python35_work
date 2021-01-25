# 获取用户输入的一个整数，输出该整数百位及以上的数字
msg = input("输入的一个整数：")
num = eval(msg)
if type(num) == type(100.1) :
    print("你输入的是浮点数！关掉重来！")
elif type(num) == type(100) :
    if 0 < num < 99 :
        print("百位=0，你输入的是小于100的数")
    elif 100 <= num :
        print("你输入的整数≥100，百位是：" + msg[-3] + "。")
