#coding=gbk
# 输入一个文件和一个字符，统计该字符在文件中出现的次数

def countstr(filename, str0) :
    f = open(filename, "rt", encoding='UTF-8')
    count = 0  # 这个字符一次也没统计，所以默认=0
    for line in f :  # 遍历row
        for i in line :  #遍历column
            if i == str0 :# 如果该row中有column等于“传入参数str1”，则计数
                count += 1
    print('“{}”字符在“{}”中出现{}次。'.format(str0,filename,count))
    f.close()

def main() :
    filename = input("输入该程序目录中的文件名：")
    str0 = input("请输入需要统计的字符：")
    countstr(filename, str0)



main()
