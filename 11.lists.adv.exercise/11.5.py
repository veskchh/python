rooms = int(input())
enough_chairs = True
for i in range(rooms):
    current_room = input().split(' ')
    if len(current_room[0]) < current_room[1]:
        print
