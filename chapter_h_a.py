# 用户输入一个年份，判断是否为闰年。
# 条件1：能被400整除
# 条件2：能被4整除但不能被100整除
year = input("请输入一个年份：")
num = eval(year)
if  (num % 400 == 0) or (num % 4 == 0 and num % 100 != 0) :
    print("这个年份是闰年")
else :
    print("这个年份不是闰年")
