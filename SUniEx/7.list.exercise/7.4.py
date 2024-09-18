list_integers = input().split(', ')
beggars = int(input())
beggars_list = []
counter = 0
temp_sum = 0
digits = [int(i) for i in list_integers]

while counter < beggars:
    for i in range(counter, len(digits), beggars):
        temp_sum += digits[i]
    beggars_list.append(temp_sum)
    temp_sum = 0