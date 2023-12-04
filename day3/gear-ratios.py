import functools

filename = input("enter a filename")
fin = open(filename, "r")
lines = fin.read().split('\n')

valid_symbols = ['*', '/', '-', '+', '&', '=', '@', '$', '%', '#']
                 
symbol_string = ''.join(valid_symbols)
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

chars = []

total_sum = 0
for index, line in enumerate(lines):
    enumerated = [elem for elem in enumerate([*line])]
    if len(line) == 0:
        break
    condensed = [enumerated[0]]
    for e in enumerated[1:]:
        if e[1].isnumeric() and condensed[-1][1].isnumeric():
            condensed[-1] = (condensed[-1][0], condensed[-1][1]+e[1])
        else:
            condensed.append(e)
    one_to_one = []
    for condense in condensed:
        for i in range(len(condense[1])):
            one_to_one.append(condense)
    print(one_to_one)
    nums_only = list(filter(lambda x: x[1].isnumeric(), condensed))
    gears_only = list(filter(lambda x: x[1] == '*', condensed))
    for num in nums_only:
        surrounding = []
        if index > 0:
            # print(f'ARR {[*lines[index-1][num[0]:num[0]+len(num[1])]]}')
            surrounding+=[*lines[index-1][num[0]:num[0]+len(num[1])]]
            if num[0] > 0:
                surrounding+=[*lines[index-1][num[0]-1]]
            if num[0]+len(num[1]) < len(line):
                surrounding+=[*lines[index-1][num[0]+len(num[1])]]
        if index < len(lines)-2:
            # print(f'ARR {[*lines[index+1][num[0]:num[0]+len(num[1])]]}')
            surrounding+=[*lines[index+1][num[0]:num[0]+len(num[1])]]
            if num[0] > 0:
                # print(f'INDEX {index} index {num[0]-1}')
                surrounding+=[*lines[index+1][num[0]-1]]
            if num[0]+len(num[1]) < len(line):
                surrounding+=[*lines[index+1][num[0]+len(num[1])]]
        if num[0] > 0:
            # print('yes')
            surrounding+=[*line[num[0]-1]]
            # print(f'NOW {surrounding}')
        if num[0]+len(num[1]) < len(line):
            # print('no')
            surrounding+=[*line[num[0]+len(num[1])]]
            # print(f'NOW {surrounding}')
        print(surrounding)
        if len([elem for elem in surrounding if elem in valid_symbols]):
            total_sum += int(num[1])

    for gear in gears_only:
        pass
print(total_sum)
    # for element in line_symbols:
    #     prev_length = len(element[1])
    #     if (stripped := element[1].strip(symbol_string)) != '':
    #         if len(stripped) < prev_length or lines[index+1][element[0]:len(stripped)+1]:
    #             total_sum += int(stripped)
