teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

card = ''

while len(teamA) > 6 and len(teamB) > 6:
    card = input()
    if card == '':
        break
    card_list = card.split('-')
    if card_list[0] == 'A':
        try:
            teamA.remove(int(card_list[1]))
        except ValueError:
            pass
    elif card_list[0] == 'B':
        try:
            teamB.remove(int(card_list[1]))
        except ValueError:
            pass


print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")

if len(teamA) <= 6 or len(teamB) <= 6:
    print('Game was terminated')