with open('./input.txt', 'r') as f:
    input = list(map(int, f.read().splitlines()))

# Part 1
a = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        a = a + 1
print(a)

# Part 2
b = 0
for j in range(0, len(input)-1):
    A = input[j-2] + input[j-1] + input[j]
    B = input[j-1] + input[j+1] + input[j]
    if A < B:
        b = b + 1
print(b)