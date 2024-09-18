is_even = lambda x: x % 2 == 0
list_num = input().split()
list_num_int = [int(i) for i in list_num]

result = list(filter(is_even, list_num_int))

print(result)
