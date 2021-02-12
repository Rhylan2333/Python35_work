import jieba

s="Python是最有意思的编程语言"

Iterator1 = jieba.cut(s)

ls=list(Iterator1)

print(ls)

print("\n{:-^20}\n".format('涉及迭代器的方法'))



Iterator2 = jieba.cut(s)
print("Iterator2的类型：", type(Iterator2), "\n输出如下：")
# Iterator2 = Iterator2.__iter__()
for i in Iterator2 :
    print(i)  # 强行可以
    print(Iterator2.__next__())  # 一次两个


print("\n{:-^20}\n".format('不涉及迭代器的方法'))  # 居中对齐优先减少左边的“-”（左5-右6-）
print("Iterator2的类型：", type(Iterator2), "\n输出如下：")
Iterator3 = jieba.cut(s)
for i in Iterator3 :  # 可以
    print(i)
