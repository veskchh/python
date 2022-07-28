rows = int(input())
sum_ascii = 0

for x in range(rows):
    char = input()
    sum_ascii += ord(char)

print(f'The sum equals: {sum_ascii}')