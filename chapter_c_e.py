# 输入一个十进制整数，分别输出其二进制、八进制、十六进制字符串
num = eval(input("输入一个十进制数，我将分别为你输出其二进制、八进制、十六进制\n："))
print("十六进制：" + hex(num))
print("八进制："+ oct(num))
# 接下来换算二进制
msg = ''
while num > 1 :  # 用“除二法”求十进制的二进制
    num, rem = divmod(num, 2)  # rem非0即1
    msg += str(rem) 
msg = '1' + msg
print('二进制：' + msg)    
