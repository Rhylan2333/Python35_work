#问题1模板：
#P301-1.py
#请在.....处填写多行表达式或语句
#可以修改其他代码

menu=["1. 显示所有信息","2. 追加信息","3. 删除信息"]
flag = True
while flag:
    for element in menu:
        print(element)
    ch = ''  # 为了使非int输入也能运行后续if语块
    try:
        ch = int(input("请输入数字1-3选择功能："))
        flag = False  # 跳出循环
    except:
        flag = True  # 继续循环
    if ch not in {1,2,3}:  # 这里的if与except处于同一层次
        print("请重新输入")
        flag = True
print("您选择了功能", ch)
