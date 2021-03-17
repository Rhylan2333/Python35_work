#在 _____上补充一行代码
#不要修改其他代码

s = input()
d = 0
while s:
    d = d + int(s[0])*pow(2,len(s)-1)
    s = s[1:]
print("转换成十进制数是：{}".format(d))
