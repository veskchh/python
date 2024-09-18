def shoot(target, current_index, current_value):
    target[current_index] -= current_value

# def add():
# def strike():


targets = [int(i) for i in input().split(' ')]
command = input().split(' ')

while command[0] != 'End':
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == "Shoot":
        if 0 <= index <= len(targets):
            shoot(targets, index, value)
    elif action == "Add":
        pass
    elif action == "Strike":
        pass

    command = input().split(' ')

print('|'.join([str(i) for i in targets]))