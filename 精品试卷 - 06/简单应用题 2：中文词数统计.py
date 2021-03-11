#请在.....处填写多行表达式或语句
#可以修改其他代码

import jieba
s = input()
s_pured = ''
expect = {'“', '，','。','、','”'}
for string in s:
    if string not in expect:
        s_pured += string
k = jieba.lcut(s_pured)
for word in k:
    print(word,end="/ ")
print("\n中文词语数是：{}".format(len(k)))
