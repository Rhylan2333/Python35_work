#编写一个函数，打印200以内的所有素数，以空格分隔
def isPrime(num) :
    """
: para num: 输入的整数
: return: 质数返回True，否则返回False
"""
    if num < 2 :
        return False
    for i in range(2, num) :
        if  num % i == 0 :
            return False
        return True



def printPrime() :
    for i in range(0, 200) :
        if (isPrime(i)) :
            print(i, end=" ")
        else :
            continue




# 接下来运行程序
printPrime()
