 #在 _____上补充一行代码 
 #在…….上补充多行代码 


ls = eval(input())
for i in range(len(ls)):
    ls[i] = ls[i].capitalize()        #将所有的字符串首字母转换成大写capitalize()函数
print(ls)
