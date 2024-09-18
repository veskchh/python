num = int(input())

for i in range(0, num):
    for x in range(0, num):
        for y in range(0, num):
            print(f'{chr(97 + i)}{chr(97 + x)}{chr(97 + y)}')