#羊车门问题的概率解答https://www.zhihu.com/question/63761789/answer/1000719021
import random 
times = eval(input("对于“羊车门问题，你想做几次模拟实验："))
first_choice_times = 0  # 初始化不改选择的次数
change_choice_times = 0  # 初始化更改选择的次数
for i in range(times) :
	car_in_Door = random.randint(1, 3)
	my_guess = random.randint(1, 3)
	if car_in_Door == my_guess:
		first_choice_times += 1
	else:
		change_choice_times += 1
print("不改选择选中车的概率：{}".format(first_choice_times / times))
print("更改选择选中车的概率：{}".format(change_choice_times / times))
