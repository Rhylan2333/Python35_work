def fact(n) :
    """求n的阶乘"""
    if n==1 :
        return 1
    return n * fact(n - 1)



num = eval(input("请输入一个正整数n，我将输出n的阶乘："))

msg = fact(num)

print(num, "的阶乘是", msg, "。")
