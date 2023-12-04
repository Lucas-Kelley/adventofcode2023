filename = input("enter a filename: ")
fin = open(filename, "r")
lines = fin.read().split('\n')
lines.pop()

total_sum = 0
original_cards = len(lines)
scratch_cards = 0
while scratch_cards < len(lines):
    line = lines[scratch_cards]
    if not len(line): break
    card_sections = line.split('|')
    part = card_sections[0].split(':')
    first = part[1].strip()
    card_number = int(part[0].split(' ')[-1].strip())
    second = card_sections[1].strip()
    winning_numbers = [elem for elem in first.split(' ') if elem.isnumeric()]
    our_numbers = [elem for elem in second.split(' ') if elem.isnumeric()]
    run_sum = 0
    for num in our_numbers:
        if num in winning_numbers:
            run_sum+=1
    # if card_number+run_sum >= original_cards:
    lines += lines[card_number:card_number+run_sum]
    scratch_cards += 1
    # print(f'WIN {winning_numbers}, OUR {our_numbers}')
    
print(scratch_cards)
