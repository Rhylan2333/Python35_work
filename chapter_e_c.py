def count_str_type(string) :
    """
:para string: 传入字符
:return: 数字、字母、空格、其他字符的个数
    """
    number_num=0
    alphabet_num=0
    space_num=0
    other_num=0
    
    for i in string :
        if ord(i) in range(48, 58) :
            number_num += 1
        elif ord(str.lower(i)) in range(97, 123) :
            alphabet_num += 1
        elif i == ' ' :
            space_num += 1
        else :
            other_num += 1
    print("\n统计结果如下：")
    print("数字个数：{}".format(number_num),\
          "\n字母个数：{}".format(alphabet_num),\
          "\n空格个数：{}".format(space_num),\
          "\n其他个数：{}".format(other_num))

        

string = input("请输入一行字符：\n")

count_str_type(string)
