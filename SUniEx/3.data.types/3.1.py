n = int(input())
for num in range(1, n + 1):
    sum = 0
    digit = num

    while digit > 0:
        sum += digit % 10
        digit = int(digit / 10)

    if sum == 5 or sum == 7 or sum == 11:
        output = True
    else:
        output = False

    print(f'{num} -> {output}')
