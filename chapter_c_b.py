# 获得用户输入的一个字符串，将字符串按照空格分割，然后逐行打印出来
msg_0 = input("请输入一个字符串：\n")
msg_1 = " ".join(msg_0)
list_msgs = msg_1.split()  # 默认split“空格”
# print(list_msgs)  # 检查。split()是否正常工作
length = len(list_msgs)
print("逐行打印如下：")
for i in range(length) :
    print(list_msgs[i])
