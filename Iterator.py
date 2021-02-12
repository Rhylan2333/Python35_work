# 学习迭代器
d = {"a": 1, "b": 2, "c": 3}
res = d.__iter__()  # 对key迭代
print("这里对dict调用__iter__()方法后：", res)
while True :
    try :
        print(res.__next__())
    except StopIteration :
        print("StopIteration，到尾了。")
        break
print("\n{:-^44}\n".format('分割线'))
# 重复执行迭代器会怎样？
# 在一个迭代器取值取干净的情况下，再对其取值，取不到
# 必须再调用一次迭代器才能取值，即更新
# 步骤： 1、调用迭代器  2、取值
res = d.__iter__()
print("对dict再调用一次__iter__()才能通过__next__()取值")
while True :
    try :
        print(res.__next__())
    except StopIteration :
        print("StopIteration，到尾了。")
        break
