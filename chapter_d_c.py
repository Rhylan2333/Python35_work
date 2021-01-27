# 统计不同字符的个数。用户从键盘输入一行字符，编写一个程序，统计并输出其中的英文字符、数字、空格和其他字符的个数。
string = input("请输入一行字符：\n")
alphabet, num, spacing, other = 0, 0, 0, 0
for i in string :
    if i.isalpha() :
        alphabet += 1
    elif i.isdigit() :
        num += 1
    elif i.isspace() :
        spacing += 1
    else :
        other+=1
print("你输入的字符串中, 有\
英文字符数{}个，数字字符数{}个，空格字符数{}个，其他字符数{}个。".format(alphabet,num,spacing,other))




text = input('再来一遍，请输入字符：')                       # 界面：让用户输入字符 
zgeshu = ygeshu = sgeshu = qgeshu = kgeshu = 0    # 设置初始值，以便用于for in循环
for i in text :
    if 40869 >= ord(i) >= 19968:                  # 本处使用十进制，简单。或者使用十六进制，再用ord('\u9fa5')转换为十进制的unicode编码；
        zgeshu += 1
    elif 57 >= ord(i) >= 48:
        sgeshu += 1
    elif 122 >= ord(str.lower(i)) >= 97:          # 直接使用str.lower()函数，将英文字符统一为小写，节省代码；
        ygeshu += 1
    elif i == ' ':
        kgeshu += 1
    else:
        qgeshu += 1
print("统计结果如下：")
print('中文字符个数为{}，'.format(zgeshu), '\n'\
      +'数字字符个数为{}，'.format(sgeshu), '\n'\
      +'英文字符个数为{}，'.format(ygeshu), '\n'\
      +'空格字符个数为{}，'.format(kgeshu), '\n'\
      +'其他字符个数为{}。'.format(qgeshu))
