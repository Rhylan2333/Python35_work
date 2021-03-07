#在_____上填写一行代码
import jieba
Tempstr = input()
ls = jieba.lcut(Tempstr)  # 精确模式
print(ls)
