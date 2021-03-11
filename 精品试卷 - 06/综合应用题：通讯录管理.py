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


# 问题2模板：
# P301-2.py
# 请在.....处填写多行表达式或语句
# 可以修改其他代码


def display():
    fi = open("address.txt", 'r')
    content = fi.read()
    print(content)
    fi.close()

menu = ["1. 显示所有信息", "2. 追加信息", "3. 删除信息"]
flag = True
while flag:
    for element in menu:
        print(element)
    ch = ''  # 为了使非int输入也能运行后续if语块
    try:
        ch = int(input("请输入数字1-3选择功能："))  # 再次对ch赋值
        flag = False  # 跳出循环
    except:
        flag = True  # 继续循环
    if ch not in {1,2,3}:  # 这里的if与except处于同一层次
        print("请重新输入")
        flag = True
    elif ch == 1:
        display()
    elif ch == 2:
        pass
    elif ch == 3:
        pass


#问题3模板
#P301-3.py
#请在.....处填写多行表达式或语句
#可以修改其他代码


def display():
    fi = open("address.txt", 'r')
    content = fi.read()
    print(content)
    fi.close()



def insertrec():
    fi = open("address.txt", 'r')
    fo = open("new_address.txt", 'w')
    origin_content = fi.read()
    fo.write(origin_content)
    write = input()
    fo.write(write + "\n")
    print("内容输出到 new_address.txt 文件中")
    fi.close()
    fo.close()



menu = ["1. 显示所有信息", "2. 追加信息", "3. 删除信息"]
flag = True
ch = ''  # 为了使非int输入也能运行后续if语块
while flag:
    for element in menu:
        print(element)
    try:
        ch = int(input("请输入数字1-3选择功能："))  # 再次对ch赋值
        flag = False  # 跳出循环
    except:
        flag = True  # 继续循环
    if ch not in {1,2,3}:  # 这里的if与except处于同一层次
        print("请重新输入")
        flag = True

if ch == 1:
    display()
elif ch == 2:
    insertrec()
elif ch == 3:
    pass
