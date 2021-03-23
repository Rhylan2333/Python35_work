#请在_____上完善一行代码

import time
t = '2019-9-2'
print(t + "是星期" + str(time.strptime(t, '%Y-%m-%d')[6]+1))
