# -*- coding:utf-8 -*-
# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


fi = open("论语.txt", "r", encoding="utf-8")
fo = open("论语-原文.txt", "w")
lines = fi.readlines()
ls = []  # 待处理列表
for line in lines:
    if line == "\n" :
        continue
    else :
        line = line.strip("\n").strip()
        ls.append(line)
for i in range(len(ls)) :
    if ls[i] == "【原文】" :
        fo.write(ls[i+1] + "\n")
    else :
        continue
fo = open("论语-原文.txt", "r")
fo.write(fo.read().strip("\n"))
fi.close()
fo.close()
