# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


fi = open("论语-原文.txt", "r")
fo = open("论语-提纯原文.txt", "w")
##IDXs = []
##for i in range(1,20) :
##    IDX = "({})".format(i)
##    IDXs.append(IDX)
##IDXs = set(IDXs)
string = fi.read()
i = 1
while i <= len(string) :  # 必须小于，不然超出范围，因为while先做后加，引锁前闭后开
    for k in range(100) :
        string = string.replace("("+str(k)+")", "")
        i += 1
    fo.write(string)
fi.close()
fo.close()
