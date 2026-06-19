input_rows = input()
input_rows = int(input_rows)
sum = 0
row = 0


while row < input_rows:
    current_row = [int(x) for x in input().split()]
    sum += current_row[row]
    row += 1
print(sum)