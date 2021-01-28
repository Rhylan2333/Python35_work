# 英文字符频率统计。编写一个程序，对给定的字符串中出现的a~z字母频率分析，忽略大小写，采用降序方式输出。
txt = input("请输入一段英文文本：")  #输入
txt = txt.lower()  # 全部小写即可忽略大小写
count = {}  # 定义一个字典
for alphabet in txt :
    if alphabet in "abcdefghijklmnopqrstuvwxyz" :
        count[alphabet] = count.get(alphabet, 0) + 1       #前是key，后是value。默认为0：若这个alphabet从未出现，count=0
items = list(count. items())  # 将字典转换为列表才可以进行排序
items.sort(key = lambda x:x[1], reverse = True)  # 根据值进行降序排序，默认是升序
print("给定字符串中a~z字母的频率统计如下：")
for i in range(len(items)) :  # 0到len(items)，不包括len(items)作为下标，循环遍历列表items中的键值，分别赋值给变量word，count
    alphabet, count = items[i]  # item是tuple
    #print(items[i])  # 用来检查每个item是否正确
    if i == len(items)-1 :
        print("{:<2}出现{:^3}次。".format(alphabet, count))  # 复习format的格式化输出
    else :
        print("{:<2}出现{:^3}次；".format(alphabet, count))
