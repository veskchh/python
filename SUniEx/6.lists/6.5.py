n = int(input())

numbers = list()
filtered = list()

for i in range(n):
    current_num = int(input())
    numbers.append(current_num)

command = input()
if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtered.append(num)
elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered.append(num)
elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered.append(num)

print(filtered)