"""
重复元素判定，编写一个函数，接受列表作为参数，
如果一个元素在列表中出现不止一次，则返回True，但不要改变原来列表的值。
同时编写调用这个函数和测试结果的程序。
"""
def Check_element(ls) :    #定义函数Lbpd(a)
    if len(ls) != len(set(ls)) :
        return True
    else :
        return False



def Printf(judgement) :
    if judgement == True :
        print("存在一个元素在列表中出现不止一次。")
    elif judgement == False :
        print("列表中元素无重复。")
    return None



lists = input("请输入一个列表list，我来判断是否存在元素重复：\n")

judgement = Check_element(lists)

Printf(judgement)
