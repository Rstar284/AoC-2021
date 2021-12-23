counts = 0
file_name = 'input.txt'
with open(file_name, "r") as fd:
    for line in fd:
        wires = line.strip().split('|')[0].strip().split(' ')
        digits = ["".join(sorted(digit)) for digit in line.strip().split('|')[1].strip().split(' ')]
        for wire in wires:
            if len(wire) in (4,2,3,7):
                for digit in digits: 
                    if ''.join(sorted(wire)) == digit:  counts += 1
                        
print(counts)

result = 0
with open(file_name, "r") as fd:
    for line in fd:
        decoding_map = {}
        wires = line.strip().split('|')[0].strip().split(' ')
        digits = ["".join(sorted(digit)) for digit in line.strip().split('|')[1].strip().split(' ')]

        for wire in wires:
            if len(wire)==4:
                decoding_map[4] = wire
            elif len(wire)==7:
                decoding_map[8] = wire
            elif len(wire)==2:
                decoding_map[1] = wire
            elif len(wire)==3:
                decoding_map[7] = wire
                
        for wire in wires:
            if len(wire)==6:
                if decoding_map[1][0] not in list(wire) or decoding_map[1][1] not in list(wire):
                    decoding_map[6] = wire

        for wire in wires:
            if len(wire)==5:
                can_be_five = True
                for digit in wire:
                    if digit not in list(decoding_map[6]):
                        can_be_five = False
                if can_be_five:
                    decoding_map[5] = wire
                    for character in decoding_map[6]:
                         if character not in decoding_map[5]:
                            difference_with_six = character
                else:
                    if (decoding_map[1][0] not in list(wire) and decoding_map[1][1] in list(wire)) or (decoding_map[1][0] in list(wire) and decoding_map[1][1] not in list(wire)) :
                        decoding_map[2] = wire
                    else:
                        decoding_map[3] = wire

        for wire in wires:
            if len(wire) == 6 and decoding_map[6] != wire:
                if difference_with_six not in list(wire):
                    decoding_map[9] = wire 
                else:
                    decoding_map[0] = wire 

        decoding_map_reversed = {"".join(sorted(value)):key for (key,value) in decoding_map.items()}
        total = 0
        for digit in digits:
            total = total*10 + decoding_map_reversed[digit]
        result += total
        
print(result)