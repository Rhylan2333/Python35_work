"""
实现isPrime()函数，参数为整数，要有异常处理。
如果整数是质数，返回True，否则返回False
https://blog.csdn.net/jwsgd/article/details/93082334?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_utm_term-2&spm=1001.2101.3001.4242
https://blog.csdn.net/Wut_LS/article/details/96719107?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161172686316780262550185%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161172686316780262550185&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-96719107.pc_search_result_before_js&utm_term=%E5%AE%9E%E7%8E%B0isprime%28%29%E5%87%BD%E6%95%B0%2C%E5%8F%82%E6%95%B0%E4%B8%BA%E6%95%B4%E6%95%B0%2C%E8%A6%81%E6%9C%89%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86&spm=1018.2226.3001.4187
"""
def isPrime(n):
    if n < 2:
        return False
    elif n == 2 or 3 :
        return True
    else:
        for i in range(2, int(pow(n, 0.5)+1)) :
            if n % i == 0 :
                return False
            else :
                return True
try :
    n = eval(input("请输入你要检测的数字："))
    if isPrime(n) :
        print("你所检测的数字是质数。")
    else :
        print("你所检测的数字不是质数。")
except :
    print("格式输入错误，请重新输入一个数字，不要加入字母和其他特殊符号")
