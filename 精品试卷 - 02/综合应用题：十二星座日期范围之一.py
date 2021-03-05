# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

csv = open("PY301-SunSign.csv", "r", encoding="utf-8")
ls = []
lines = csv.readlines()
for i in range(len(lines)) :
    row = lines[i].replace("\n","").split(",")
    ls.append(row)
s = input("请输入星座中文名称(例如, 双子座):")
for i in range(len(ls)) :
    if s == ls[i][1] :
        print("{}的生日位于{}-{}之间".format(s, ls[i][2], ls[i][3]))
