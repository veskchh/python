def reverse(num):
    reverse_num = num[::-1]
    return reverse_num


def pali_checker(listt):
    for i in listt:
        if i == reverse(i):
            print('True')
        else:
            print('False')


qko = input().split(', ')

pali_checker(qko)
