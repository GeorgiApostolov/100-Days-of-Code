input_strings = [str(x) for x in input().split()]
output_dict = dict()
for string in input_strings:
    if string in output_dict:
        output_dict[string] += 1
    else:
        output_dict[string] = 1

for key in output_dict:
    value = output_dict[key]
    print(f"{key} -> {value}")