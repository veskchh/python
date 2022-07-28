command = input()
numbers = {}
while not command.isdigit():
    number = command.split('-')
    numbers[number[0]] = number[1]
    command = input()

command = int(command)

for i in range(command):
    request = input()
    if request in numbers.keys():
        print(request + ' -> ' + numbers[request])
    else:
        print(f'Contact {request} does not exist.')