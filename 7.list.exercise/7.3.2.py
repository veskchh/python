teamA = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
teamB = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_term = False

cards_1_by_1 = input().split(' ')
for player in cards_1_by_1:
    if player in teamA:
        try:
            teamA.remove(player)
        except ValueError:
            pass
    elif player in teamB:
        try:
            teamB.remove(player)
        except ValueError:
            pass
    if len(teamA) < 7 or len(teamB) < 7:
        game_term = True
        break


print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")

if game_term:
    print('Game was terminated')