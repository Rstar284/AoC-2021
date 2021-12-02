with open('input.txt', 'r') as f:
    input = f.read().splitlines()

x = y = depth = depth1 = 0

for line in input:
    cmd,num = line.split()
    num = int(num)
    if cmd == 'forward':
        y += num
        depth1 += x * num
    if cmd == 'up' :
        x -= num
        depth -= num
    if cmd == 'down':
        x += num
        depth += num

print(y * depth)
print(y * depth1)



