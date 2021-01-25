# 设n是一任意自然数，如果n的各位数字反向排列所得自然数与n相等，则n被称为回文数。从键盘输入一个5位数字，请编写程序判断这个数字是不是回文数。
msg = input("请输入一个五位数：")
num = eval(msg)
if len(msg) == 5 :
    msg = " ".join(msg)
    list_msgs = msg.split()
    # print(list_msgs)
    list_msg_res = []
    for i in range(len(list_msgs)) :
        a = list_msgs[len(list_msgs)-(i+1)]
        list_msg_res.append(a)
    if  list_msgs == list_msg_res :
        print("是回文数。")
    else :
        print("不是回文数。")
else :
    print("按规定来，我还不会处理那么多！")
