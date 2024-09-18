command = input()
things = {}
while command != 'stop':
    quantity = int(input())
    resource = command
    if resource not in things:
        things[resource] = 0
    things[resource] += quantity
    command = input()

for k,v in things.items():
    print(f'{k} -> {v}')