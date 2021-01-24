# CaesarChineseDecode.py

p_txt = input("请输入明文文本：（英文字母、汉字会被解密）\n")
"""解密原理：Unicode码左移3位"""
for p in p_txt :
    if "a" <= p <= "z" :
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26), end='')  # 取余，ord(x)返回单字符x表示的Unicode编码
    elif "A" <= p <= "Z" :
        print(chr(ord("A")+(ord(p)-ord("A")-3)%26), end='')  # 取余，chr(x)返回Unicode编码x表示的单字符
    elif 0x4E00 <=ord(p) <= 0x9FA5 :  # 中文字符解密处理
        # print(chr(ord(p)-3), end='')
        print(chr(ord("一")+(ord(p)-ord("一")-3)%20902), end='')
    else :
        print(p, end='')
