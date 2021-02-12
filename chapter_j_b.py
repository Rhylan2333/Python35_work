# 使用jieba.cut()对“今天晚上我吃了意大利面”进行分词，输出结果，并使“意大利面”作为一个词出现在结果中。
import jieba
s = "今天晚上我吃了意大利面"
jieba.add_word("意大利面")

Is1 = jieba.lcut(s, cut_all=True)
print("\n使用lcut(s, cut_all=True)：", type(Is1))
print(Is1)

ls2 = jieba.lcut(s)
print("\n使用lcut()：", type(ls2))
print(ls2)

ls3 = jieba.lcut_for_search(s)
print("\n使用lcut_for_search(s)：", type(ls3))
print(ls3)
