num = int(input())

for x in range(num):
    print('*' * (x + 1))
for y in range(num - 1, 0, -1):
    print('*' * y)
