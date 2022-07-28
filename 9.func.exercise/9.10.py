def perfect_num_check(num):
    dividers = []
    for i in range(1, num):
        if num % i == 0:
            dividers.append(i)
    if num == sum(dividers):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num_try = int(input())
perfect_num_check(num_try)