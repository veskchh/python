num = float(input())

if num == 0:
    print("zero")
elif num > 0:
    if num < 1:
        print('small positive')
    elif 1 < num < 1000000:
        print('positive')
    elif num > 1000000:
        print('large positive')
else:
    if num > -1:
        print('small negative')
    elif -1 > num > -1000000:
        print('negative')
    elif num < -1000000:
        print('large negative')
