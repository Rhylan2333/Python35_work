# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

csv = open("PY301-SunSign.csv", "r", encoding="utf-8")
ls = []
lines = csv.readlines()
for i in range(len(lines)) :
    row = lines[i].replace("\n","").split(",")
    ls.append(row)  # 构建矩阵
s = input("请输入星座序号(例如,5 10):")  # 是序号不是月日，仔细审题
while s != '' :
    ls_num = s.split()
    numbers = []
    for row in ls[1:]:  # “序号”是突破点
        numbers.append(row[0])
    for i in ls_num :
        if i in numbers:
            index = int(i)
            print("{}({})的生日是{}月{}日至{}月{}日之间".format(ls[index][1], ls[index][4], ls[index][2][:-2], ls[index][2][-2:], ls[index][3][:-2], ls[index][3][-2:]))
            continue
        else:
            print("输入星座序号有误！")
            continue
    s = input("请输入星座序号(例如,5 10):")
csv.close()
