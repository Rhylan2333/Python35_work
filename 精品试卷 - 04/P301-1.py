#编程模板1：P301-1.py
# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

with open("data.txt", "r", encoding="utf-8") as txt:  # 此处可多行
    rows = txt.readlines()  # 得到列向量

f = open("univ.txt", "w")
matrix = []
for row in rows[409:1074:3]:
    matrix.append(row)  # 好找
for row in matrix:
    univ = row.split("alt=")[-1].split("\"")[1]  # 第四个元素就是 alt="华东师范大学"
    f.write(univ + "\n")# 此处可多行
f.close()
