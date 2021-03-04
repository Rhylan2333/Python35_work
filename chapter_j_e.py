# 出场人物词频排名，并绘制词云https://blog.csdn.net/xtingjie/article/details/71210182
import jieba as j
from wordcloud import WordCloud

filename = "chapter_j_d.txt"
# 先在excludes中填几个词，不断运行程序，从结果中选出不符的词加到excludes中，逐渐完善

f = open(filename, "r", encoding='UTF-8' )
txt = f.read()
f.close()

excludes = {'我们','一个','他们','这个','机器','没有','可以',\
        '问题','一些','就是','工作','这些','但是','不是',\
        '自己','已经','这种','因为','这样','现在','需要',\
        '什么','一种','还有','数学','想法','进行','如果',\
        '研究','非常','来说','这是','而且','知道',\
        '一样','可能','认为','关于','计算','系统','对于',\
        '不同','无法','然后','开始','那么','完全',\
        '能够','东西','密码','世界','使用','科学','所有',\
        '通过','任何','过程','一起','方法','只是','计算机',\
        '那些','很多','得到','所以','信息','物理','必须',\
        '谜机','仍然','比如','这里','喜欢','大脑','理论',\
        '人类','人们','之后','设计','战争','也许','方面',\
        '讨论','证明','不能','重要','虽然','指令','实验室',\
        '项目','它们','产生','存在','解决','其它','一位',\
        '学校','时间','觉得','应该','学院','数学家','一次',\
        '论文','状态','电子','逻辑','方式','其中','两个',\
        '看到','然而','国家','通信','一直','一点','之间',\
        '如何','海军','提出','关系','结果','希望','描述',\
        }

words = j.lcut(txt)  # 取词

def draw_wordcloud() :
    #global words, excludes  # 声明global变量，不波及外部
    for word in words :
        if len(word) == 1 :  # 排除words中的单个词，并把它填入传进来的外部global的excludes，而不改变外部excludes
            excludes.add(word)
        else :
            continue

    new_txt = ' '.join(words)  # 分词

    wordcloud = WordCloud(background_color="white",\
                      width=800, height=600,\
                      font_path='C:\Windows\Fonts\HGPTY_CNKI.TTF',\
                      max_words=200,\
                      max_font_size=80,\
                      stopwords=excludes,\
                      ).generate(new_txt)
    
    wordcloud.to_file('图灵传基本词云.png')
    return None

def show_frequency() :
    """展示词频统计表"""
    #global words, excludes  # 没有用global语句的情况下，是不能修改全局变量的
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
    return None



show_frequency()
draw_wordcloud()