vowels = "aeiou"
count = 0
input_string = input("Enter a string: ")
for char in input_string:
    if char in vowels:
        count += 1
print(count)