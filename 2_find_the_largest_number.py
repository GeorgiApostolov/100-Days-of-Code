input_numbers = [int(x) for x in input().split()]
max_number = input_numbers[0]

for curr_num in input_numbers:
    if curr_num > max_number:
        max_number = curr_num
print(max_number)