count = 0
with open("input.txt", "r") as input:
    for line in input:
        decode = {}
        wires = line.strip().split("|")[0].strip().split(" ")
        nums = ["".join(sorted(num)) for num in line.strip().split("|")[1].strip().split(" ")]
        for wire in wires:
            if len(wire) in (4,2,3,7):
                for num in nums:
                    if "".join(sorted(wire)) == num: count += 1
            if len(wire) == 4: decode[4] = wire
            elif len(wire) == 7: decode[8] = wire
            elif len(wire) == 2: decode[1] = wire
            elif len(wire) == 3: decode[7] = wire
            elif len(wire) == 6: 
                if decode[1][0] not in list(wire) or decode[1][1] not in list(wire): decode[6] = wire
            elif len(wire) == 5: 
                isfive = True
                for num in wire:
                    if num not in list(decode[6]):
                        isfive = False
                if isfive:
                    decode[5] = wire
                    for c in decode[6]:
                        if c not in decode[5]:
                            dif6 = c
                else:
                    if (decode[1][0] not in list(wire) and decoding_map[1][1] in list(wire)) or (decoding_map[1][0] in list(wire) and decoding_map[1][1] not in list(wire)) :
                        decode[2] = wire
                    else:
                        decode[3] = wire
            elif len(wire) == 6 and decoding_map[6] != wire:
                if dif6 not in list(wire):
                    decode[9] = wire 
                else:
                    decode[0] = wire
    
    print(count)
    res = 0
    count = 0
    decode_rev = {"".join(sorted(val)): key for (key,val) in decode.items()}
    for num in nums:
        count = count*10 + decode_rev[num]
    res += count
    print(res)
    
