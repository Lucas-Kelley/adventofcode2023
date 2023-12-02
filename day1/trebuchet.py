fin = open("input", "r")
lines = fin.read().split('\n')

def string_to_num(string):
    match string:
        case '1' | 'one':
            return 1
        case '2' | 'two':
            return 2
        case '3' | 'three':
            return 3
        case '4' | 'four':
            return 4
        case '5' | 'five':
            return 5
        case '6' | 'six':
            return 6
        case '7' | 'seven':
            return 7
        case '8' | 'eight':
            return 8
        case '9' | 'nine':
            return 9

possible = ['1','2','3','4','5','6','7','8','9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total_sum = 0
for line in lines:
    if len(line) == 0:
        continue
    first = line[0]
    findex = 1
    old_index = 1
    old_index_back = 1
    bindex = 1
    last = line[-1]
    print(f'LINE: {line}')
    # for i in range(1, len(line)):
    while True:
        print (f'FIRST: {first}, LAST: {last}')
        if first in possible and last in possible:
            break
        if first not in possible:
            if first + line[findex] in [elem[:len(first)+1] for elem in possible]: # If we are still building a possibility
                if len(first) == 1:
                    old_index = findex
                first = first + line[findex]
            else: # restart
                findex = old_index
                old_index+=1
                first = line[findex]
            findex+=1
        if last not in possible:
            if line[-1*(bindex+1)] + last in [elem[-1*(len(last)+1):] for elem in possible]:
                if len(last) == 1:
                    old_index_back = bindex
                last = line[-1*(bindex+1)] + last
            else:
                bindex = old_index_back
                old_index_back += 1
                last = line[-1*(bindex+1)]
            bindex+=1
    print(f'TWO DIGIT: {(string_to_num(first)*10)+string_to_num(last)}')
    total_sum += (string_to_num(first)*10)+string_to_num(last)
    
print(total_sum)
