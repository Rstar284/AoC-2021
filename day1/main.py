with open('./input.txt', 'r') as f:
    input = list(map(int, f.read().splitlines()))

# Part 1
a = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        a = a + 1

print(a)