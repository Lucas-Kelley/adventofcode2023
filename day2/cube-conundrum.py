fin = open('input', 'r')
lines = fin.read().split('\n')

constraints = {'red': 12, 'green': 13, 'blue': 14}

def get_product(min_set):
    red = min_set['red']
    green = min_set['green']
    blue = min_set['blue']
    return red*green*blue

total_sum = 0
for line in lines:
    if not len(line):
        break
    game_stats = line[5:].split(':')
    game_number = int(game_stats[0])
    game_sets = game_stats[1].strip().split('; ')
    game_list = [{pair[1]:int(pair[0]) for pair in [p.split(' ') for p in elem.split(', ')] } for elem in game_sets]
    bad_game = False
    min_set = {'red': 0, 'green': 0, 'blue': 0}
    for game_set in game_list:
        for color, value in game_set.items():
            # if value > constraints[color]:
            #     bad_game = True
            #     break
            if value > min_set[color]:
                min_set[color] = value
    total_sum+=get_product(min_set)

print(total_sum)
