# 词频统计
import jieba as j

filename = "chapter_j_c.txt"

excludes = {'我们'}

f = open(filename, "r", encoding='UTF-8' )
txt = f.read()
f.close()

words = j.lcut(txt)

counts = {}

for word in words :
    if len(word) == 1 :  # 排除单个词
        continue
    else :
        counts[word] = counts.get(word, 0) +1

for word in excludes :  # 剔除不想统计的词
    del(counts[word])

ls_items = list(counts.items())  # 获取统计dict

ls_items.sort(key = lambda x:x[1], reverse=True)  # 按列表中元素的第二个值排降序

print("{:<10}{:>5}".format("词", "出现频数"))
print("{:-^17}".format(''))
for i in range(20) :
    word, count = ls_items[i]
    print("{0:<10}{1:>5}".format(word, count))
