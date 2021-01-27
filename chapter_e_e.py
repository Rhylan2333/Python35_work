# 编写一个函数，参数为一个整数n，获取斐波那契数列中的第n个数并返回
def CalFibonacci(n) :
    """
: para n: 正整数n
: return: 斐波那契数列中的第n个数
"""
    try :
        if n in (1, 2) :
            return n
        else :
            return CalFibonacci(n-2) + CalFibonacci(n-1)
    except :
        print("请输入正整数，如1、2......")

num = eval(input('请输入正整数n，我将返回斐波那契数列中的第n个数：'))
print(CalFibonacci(num))
