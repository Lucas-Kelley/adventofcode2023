filename = input("enter a filename: ")
fin = open(filename, "r")
lines = fin.read().split('\n')

total_sum = 0

for line in lines:
    if not len(line): break
    card_sections = line.split('|')
    first = card_sections[0].split(':')[1].strip()
    second = card_sections[1].strip()
    winning_numbers = [elem for elem in first.split(' ') if elem.isnumeric()]
    our_numbers = [elem for elem in second.split(' ') if elem.isnumeric()]
    run_sum = 0
    for num in our_numbers:
        if num in winning_numbers:
            if not run_sum:
                run_sum = 1
            else:
                run_sum *= 2
    total_sum += run_sum
    # print(f'WIN {winning_numbers}, OUR {our_numbers}')
print(total_sum)
