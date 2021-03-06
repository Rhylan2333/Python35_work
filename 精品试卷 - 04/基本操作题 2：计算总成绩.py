#请在__________上补充完成一行代码
#不改变已有的编程框架内容
with open("data.txt","r",encoding="utf-8") as fi:
  line = fi.readline().split(',')
  sum = 0
  for i in line[1:]:
      sum += int(i)
  print(sum)
