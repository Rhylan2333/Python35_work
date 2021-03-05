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
s = input("请输入星座序号(例如,5 10):")
while s != '' :
    ls_num = s.split()  #分开月 日
    if len(ls_num) != 2 or (int(ls_num[0]) not in range(1,13)) or (int(ls_num[1]) not in range(1,32)):
        print("输入星座序号有误！")
    else :
        for row in ls[1:]:  # “序号”是突破点
            if ls_num[0] == row[2][:-2] and int(ls_num[1]) >= int(row[2][-2:]) :
                print("{}({})的生日是{}月{}日至{}月{}日之间".format(row[1], row[4], row[2][:-2], row[2][-2:], row[3][:-2], row[3][-2:]))
            elif ls_num[0] == row[3][:-2] and int(ls_num[1]) <= int(row[3][-2:]) :
                print("{}({})的生日是{}月{}日至{}月{}日之间".format(row[1], row[4], row[2][:-2], row[2][-2:], row[3][:-2], row[3][-2:]))
        s = input("请输入星座序号(例如,5 10):")
    s = input("请输入星座序号(例如,5 10):")
csv.close()
