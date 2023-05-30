import random

# 生成10个随机整数（1-10之间），存入列表中
num_list = [random.randint(1, 10) for i in range(10)]
print('生成的随机数：', num_list)

# 统计每个数字出现的次数
count_dict = {}
for num in num_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 输出每个数字出现的次数
for num, count in count_dict.items():
    print(f'{num}出现了{count}次')
