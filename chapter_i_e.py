# 用time库将当前日期转化成类似“Sunday，8. January 2017 11:03 PM”的格式
import time

lctime = time.localtime()

t = time.strftime("%A，%d. %B %Y %I:%M %p", lctime)

print(t)
