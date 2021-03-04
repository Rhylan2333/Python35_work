"""
简单应用题 2：员工工资表
"""

#请在____处写一行表达式
#请在…处写多行代码
#可以修改其他代码

members = {'张三':['人力部',5500],
            '李四':['后勤部',4500],
            '王三':['市场部',6500],
            '赵六':['开发部',8500]
           }
sal_dep = {}
for key in members :  # 只遍历key，不输出value
    name = key
    salary = members[key][1]
    department = members[key][0]
    print('{}的工资是:{}, 部门是{}'.format(name, salary, department))
    sal_dep[salary] = department  # key=工资，value=部门，目的为了之后用max()取dict中最大的key

max_name = sal_dep[max(sal_dep)]
max_val = max(sal_dep)
print('工资最高的部门是:{},该部门工资是:{}'.format(max_name,max_val))
