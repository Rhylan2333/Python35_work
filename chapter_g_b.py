# 假设有一个英文文本文件，编写一个程序读取其内容并将里面的大写字母变成小写字母，小写字母变成大写字母

def main() :
    filename = input("请输入文件名称（无需后缀）：")
    transform(filename)

def transform(filename) :
    filename = filename + ".txt"
    f = open(filename,"rt")
    f_transformed = open("{}_transformed.txt".format(filename), "x")
    for line in f :
        for c in line :
            if ord(c) in range(97,123) :
                c = c.upper()
            elif ord(c) in range(65,91) :
                c = c.lower()
            f_transformed.write(c)
    f.close()
    f_transformed.close()
    print('处理完成，文件名为“{}_transformed.txt”，位于同根目录。'.format(filename))
 


main()
