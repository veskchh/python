def odd_even_sum(num):
    odd = 0
    even = 0
    list_num = [int(i) for i in str(num)]
    for i in list_num:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    print(f'Odd sum = {odd}, Even sum = {even}')


string = int(input())
odd_even_sum(string)