# 输入一个年份，判断是否为闰年
num = eval(input("输入一个年份，我来判断闰年与否："))
quotient = num%4
if quotient == 0 :
    print(str(num), "是闰年。")
else :
    print(str(num), "不是闰年。")
