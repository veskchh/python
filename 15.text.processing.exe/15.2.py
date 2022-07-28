string = input().split()
first_str = string[0]
second_str = string[1]

difference = abs(len(first_str) - len(second_str))
total_sum = 0
if len(first_str) > len(second_str):
    for i in range(0, len(second_str)):
        total_sum += ord(first_str[i]) * ord(second_str[i])
    for i in range(len(first_str) - difference, len(first_str)):
        total_sum += ord(first_str[i])
elif len(second_str) > len(first_str):
    for i in range(0, len(first_str)):
        total_sum += ord(first_str[i]) * ord(second_str[i])
    for i in range(len(second_str) - difference, len(second_str)):
        total_sum += ord(second_str[i])
else:
    for i in range(0, len(first_str)):
        total_sum += ord(first_str[i]) * ord(second_str[i])
print(total_sum)