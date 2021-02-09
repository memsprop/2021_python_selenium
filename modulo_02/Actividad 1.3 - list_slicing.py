list1 = [5, 10, 15, 20, 25, 50, 20]
my_index = 0
for i in list1:
    if i == 20:
        list1[my_index] = 200
    my_index = my_index + 1

print('Replaced nums = 20 for 200', list1)
print(list1[2:6])