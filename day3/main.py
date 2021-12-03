with open('input.txt', 'r') as f:
    input = f.readlines()
    bits = [0] * len(input[0].strip())
    eps = ""
    gam = ""
    for line in input:
        line = line.strip()
        for i in range(len(line)):
            bits[i] += int(line[i])
    for bit in bits:
        if bit > len(input)/2:
            gam += "1"  
            eps += "0"
        else:
            gam += "0"
            eps += "1"
    print(int(eps,2) *int(gam, 2))


   
