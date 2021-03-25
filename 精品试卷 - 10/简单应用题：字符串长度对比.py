#请在.....完善多行代码

#Percentage函数返回字符串str1与str2中按位置对应字符比较，比较相同的数目与字符串总长度的百分比
#请阅读函数功能，在....中直接调用该函数即可。
def Percentage(str1,str2):
    n = 0
    for s1,s2 in zip(str1,str2):
        if s1 == s2:
            n += 1
    return  n/len(str1)

s1 = "我爱你中国"
print(s1)
s2 = input()

if len(s2) == len(s1):  #完善多行代码
    persentage = Percentage(s1, s2)
    print("{:.2%}".format(persentage))
elif len(s2) != len(s1):
    print("输入字符串长度不一致，请重新运行本程序！")
