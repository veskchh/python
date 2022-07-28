int1 = int(input())
int2 = int(input())
int3 = int(input())


def add_and_subtract():
    def sum_numbers():
        return int1 + int2

    print(sum_numbers() - int3)


add_and_subtract()