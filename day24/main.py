import sys

def parse(l):
    strings = l.strip().split()
    return (strings[0], strings[1:])

with open('input', 'r') as f:
    program = [parse(l) for l in f.readlines()]

min_digits = [None] * 14
max_digits = [None] * 14

stack = []
for digit in range(14):
    div_op = program[digit * 18 + 4]
    if div_op[1][1] == '1':
        add_op = program[digit * 18 + 15]
        stack.append((digit, int(add_op[1][1])))
    elif div_op[1][1] == '26':
        add_op = program[digit * 18 + 5]
        old_digit, x = stack[-1]
        stack = stack[:-1]
        difference = x + int(add_op[1][1])

        if difference > 0:
            max_digits[digit] = 9
            max_digits[old_digit] = 9 - difference

            min_digits[digit] = 1 + difference
            min_digits[old_digit] = 1
        else:
            max_digits[digit] = 9 + difference
            max_digits[old_digit] = 9

            min_digits[digit] = 1
            min_digits[old_digit] = 1 - difference
    else:
        raise Exception()

print()
print(''.join([str(x) for x in max_digits]))
print(''.join([str(x) for x in min_digits]))