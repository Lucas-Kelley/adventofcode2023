import functools

filename = input("enter a filename: ")
fin = open(filename, "r")
lines = fin.read().split('\n')

gear = '*'
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

formatted = []
total_sum = 0
for line in lines:
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
    formatted.append(one_to_one)
    # gears_only = list(filter(lambda x: x == '*', condensed))

    # for gear in gears_only:
    #     pass
for index, fline in enumerate(formatted):
    gears_only = list(filter(lambda x: x[1][1] == '*', enumerate(fline)))
    for gindex, gear_tuple in gears_only:
        surrounding = set()
        if index > 0:
            surrounding.add(formatted[index-1][gindex])
            if gindex > 0:
                surrounding.add(formatted[index-1][gindex-1])
            if gindex+1 < len(fline):
                surrounding.add(formatted[index-1][gindex+1])
        if index < len(formatted)-1:
            surrounding.add(formatted[index+1][gindex])
            if gindex > 0:
                surrounding.add(formatted[index+1][gindex-1])
            if gindex+1 < len(fline):
                surrounding.add(formatted[index+1][gindex+1])
        if gindex > 0:
            surrounding.add(formatted[index][gindex-1])
        if gindex+1 < len(fline):
            surrounding.add(formatted[index][gindex+1])
        filtered = list(filter(lambda x: x[1].isnumeric(), list(surrounding)))
        # print(f'SURROUNDING {surrounding}, FILTERED {filtered}')
        if len(filtered) == 2:
            total_sum += int(filtered[0][1])*int(filtered[1][1])
    
# print(formatted)
print(total_sum)
