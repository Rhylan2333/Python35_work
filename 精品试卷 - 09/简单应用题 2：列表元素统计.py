#请在......处填写多行代码
#请在_______处填写一行代码

def is_prime(n):
    for i in range(2, n):  # 只能被除1与自己整除，就是素数
        if n % i == 0:
            return False  # 不是素数返回True
        else:
            continue  # 不能被整除则继续
    return True  # 是素数则返回True

ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime(i) == True:
        ls.remove(i)
print(len(ls))