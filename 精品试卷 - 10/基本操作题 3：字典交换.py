#在......上填写一段代码

def reverse_dict(dic):
    out_dic = {}
##    print(dic.items())
    for key, value in dic.items():
##        print(key, value)
        out_dic[value] = key
    keys = sorted(out_dic.keys(), reverse = True)  # 返回一个列表
##    print(keys)
    for key in keys:
        print(key, out_dic[key])
    return out_dic

#请输入一个字典
dic = eval(input(""))
reverse_dict(dic)
