# CalFibonacci.py
# 求斐波那契数列中小于1000的所有数
a, b = 0, 1
print("一下是契数列中小于1000的数：")
while a < 1000:
    print(a, end=', ')
    a, b = b, a+b
