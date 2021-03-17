#在_____上填写一行代码
#在……上填写一段代码

fp = open("out.txt", 'w')
ch = input("请输入字符串：\n")
while ch:
    if '@' in ch:
        t = ch.index("@")  # find()函数是字符串查找函数
        fp.write(ch[0:t])  # 截取"@"之前的字符，写入文件。
        break
    else:
        fp.write(ch + " ")
    ch = input('')
fp.close()
