# -*- coding:utf-8 -*-
# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

#此处可多行
#对数据进行中文分词处理
import jieba
f = open('out1.txt','w')
fi = open("data.txt","r",encoding="utf-8")
origin_words_list = jieba.lcut(fi.read())
words_set = set(origin_words_list)
ordered_words_set = sorted(words_set)
ordered_word_list = list(ordered_words_set)
'''现在输出'''
for word in ordered_word_list:
    if len(word) >= 3:
        f.write(word+'\n')
    else:
        continue
fi.close()
f.close()
