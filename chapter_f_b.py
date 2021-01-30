# 中文字符频率统计。编写一个程序，对给定字符串中出现的全部字符（含中文字符）频率进行分析，采用降序方式输出
string = input("请输入一段文本：")
counts = {}
for char in string :
    counts[char] = counts.get(char, 0) + 1  # 遍历counts字典中的key，没有则创建并对其value“加1”；否则只加一
items = list(counts.items())  # 将counts字典转变为list（元素是tuple）以接下来对其key排序
items.sort(key = lambda x:x[1], reverse = True)  # 排序用，不必深究，背会。reverse = True为降序（从大到小）
for i in range(0, len(items)) :
    zifu , count = items[i]  # zifu只用于传递给下一行代码
    print("“{}”出现了{:^5}次".format(zifu, count))
