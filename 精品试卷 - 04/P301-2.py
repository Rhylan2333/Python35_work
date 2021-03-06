#编程模板2：PY301-2.py
# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

n = 0
m = 0

f = open("univ.txt", "r")
lines= f.read().split("\n")
for univ in lines:  # 此处可多行
    if "大学" not in univ and "学院" not in univ:  # 用 if ("大学"or"学院") not in univ: 得不到学院，因从左读 python不懂or要两个都试一遍。应if "大学" not in univ and "学院" not in univ:
        continue
    elif "大学生" in univ:
        continue
    elif "大学" in univ and "学院" in univ:  # 用 elif ("大学"and"学院") in univ: 得不到。应elif "大学" in univ and "学院" in univ:
        if univ.index("大学") > univ.index("学院"):
            n += 1
            print(univ)
        elif univ.index("学院") > univ.index("大学"):
            m += 1
            print(univ)
    elif "学院" in univ:
        m += 1
        print(univ)
    elif "大学" in univ:
        n += 1
        print(univ)

f.close()

print("包含大学的名称数量是{}".format(n))
print("包含学院的名称数量是{}".format(m))
