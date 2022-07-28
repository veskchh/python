def sort(list_numo):
    sorted_list = sorted(list_numo)
    print(sorted_list)


list_num = input().split()
list_num_int = [int(i) for i in list_num]

sort(list_num_int)