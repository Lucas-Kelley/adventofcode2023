fin = open('input', 'r')
lines = fin.read().split('\n')

constraints = {'red': 12, 'green': 13, 'blue': 14}

total_sum = 0
for line in lines:
    if not len(line):
        break
    game_stats = line[5:].split(':')
    game_number = int(game_stats[0])
    game_sets = game_stats[1].strip().split('; ')
    game_list = [{pair[1]:int(pair[0]) for pair in [p.split(' ') for p in elem.split(', ')] } for elem in game_sets]
    bad_game = False
    for game_set in game_list:
        for color, value in game_set.items():
            if value > constraints[color]:
                bad_game = True
                break
        if bad_game:
            break
    if bad_game:
        continue
    total_sum+=game_number

print(total_sum)
