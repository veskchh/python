string = input()

string_list = string.split(' ')


for i in range(len(string_list) - 1, -1, -1):
    string_list[i] = int(string_list[i]) * -1

print(string_list)