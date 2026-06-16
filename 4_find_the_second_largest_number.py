# vhod 5 17 3 44 21 8

input_numbers = [int(x) for x in input().split()]
biggest_num = 0
second_num = 0
great_num = 0

for number in input_numbers:
    if number > biggest_num:
        second_num = biggest_num
        biggest_num = number
    elif number > second_num:
        second_num = number
print(second_num)
