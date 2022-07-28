path_list = input().split("\\")

file = path_list[len(path_list) - 1].split('.')
print(f"File name: {file[0]}\nFile extension: {file[1]}")