"""
猜数游戏续。对于程序练习题4.4程序，当用户输入的不是整数（如字母、浮点数）时，程序会终止执行退出。
改编该程序，当用户输入出错时，给出“输入内容必须为整数！”的提示，并让用户重新输入。
"""
import random
target = random.randint(1, 1000)

count = 0
while True:
    try:
        guess=eval(input("请输入一个猜测的整数（1~1000）："))
        if guess < target :
            print("猜小了")
        elif guess > target :
            print("猜大了")
        else:
            print("猜了{}次，你猜中了。".format(count))
            break
    except:
        print("输入内容必须为整数，重新输入，此次输入不计入猜测数。")
        continue
    count += 1
