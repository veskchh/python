string = input()
result = ''
for i in range(0, len(string)):
    if string[i] not in result or string[i] != string[i - 1]:
        result += string[i]

print(result)