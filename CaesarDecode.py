# CaesarDecode.py

p_txt = input("请输入明文文本：（英文字母会被解密）\n")
"""26个字母循环左移3位，即往前3个"""
for p in p_txt :
    if "a" <= p <= "z" :
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26), end='')  # 取余，ord(x)返回单字符x表示的Unicode编码
    elif "A" <= p <= "Z" :
        print(chr(ord("A")+(ord(p)-ord("A")-3)%26), end='')  # 取余，chr(x)返回Unicode编码x表示的单字符
    else :
        print(p, end='')
