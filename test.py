count = int(input())
#print(count)
list= []
i = 0
for x in range(count):
    inputs = float(input())
    list.append(inputs)
#print(list, end='')
max_num = max(list)
#print(max_num)
for number in list:
    your_value = number / max_num
    print(f'{your_value:.2f}')