"""
Python 实现isNum函数，参数作为一个字符串，
如果这个字符串属于整数、浮点数、或复数的表示，
则返回True，否则返回False。
"""
msg = input("请输入一个字符串（属于整数、浮点数、或复数）：")



def isNum(string) :
    try :
        num = eval(string)
        if type(num) == float\
           or type(num) == int\
           or type(num) == complex :
            return True
        else :
            return False
    except:
        print("请输入“数”！")  # 防止n="非数字，eval()后报错"



isNum(msg)
