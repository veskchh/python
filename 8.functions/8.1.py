def abs_list():
    abs_num_list = []
    num_list = input().split(' ')
    for i in num_list:
        abs_num_list.append(abs(float(i)))
    print(abs_num_list)


abs_list()