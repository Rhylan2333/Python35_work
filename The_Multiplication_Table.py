# The_Multiplication_Table.py
# 九九乘法表
for i in range(1,10):  # 很像线性代数的“i行”
    for j in range(1,i+1):  # 嵌套的遍历，很像线性代数的“j列”
        """# 这里的{:2}是为了限定输出的字符串长度，如果“<2”则在前面添个空的直到是2"""
        print("{}*{}={:2}".format(\
                                    j,\
                                    i,\
                                    i*j),\
              end=', ')
    print('')
