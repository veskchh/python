string = input()
strength = 0
new_string = ''

for index in range(0, len(string)):
    if string[index] != '>' and strength > 0:
        strength -= 1
    elif string[index] == '>':
        strength += int(string[index + 1])
        new_string += string[index]
    else:
        new_string += string[index]


print(new_string)