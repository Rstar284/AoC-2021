from collections import defaultdict

with open('./input.txt') as f:
	lines = [line.strip() for line in f.readlines()]

def bit_criteria(lines):
	bit_counts = dict()
	for line in lines:
		for i, c in enumerate(line):
			bit_counts[i] = bit_counts.get(i, dict())
			bit_counts[i][c] = bit_counts[i].get(c, 0) + 1
	return bit_counts

bit_counts = bit_criteria(lines)
bit_counts1 = bit_counts
lines1 = lines.copy()
o2 = -1
co2 = -1

for i in range(len(lines[0])):
	max_bit = max(bit_counts[i].items(), key=lambda i: i[1])[0]
	min_bit = min(bit_counts1[i].items(), key=lambda i: i[1])[0]
	if bit_counts[i].get('0', 0) == bit_counts[i].get('1', 0):
		max_bit = '1'
	if bit_counts1[i].get('0', 0) == bit_counts1[i].get('1', 0):
		min_bit = '0'   
	if o2 == -1:
		lines = [line for line in lines if line[i] == max_bit]
		bit_counts = bit_criteria(lines)
		if len(lines) == 1:
			o2 = int(lines[0], base=2)
	if co2 == -1:
		lines1 = [line for line in lines1 if line[i] == min_bit]
		bit_counts1 = bit_criteria(lines1)
		if len(lines1) == 1:
			co2 = int(lines1[0], 2)

	if o2 != -1 and co2 != -1:
		break

print(o2 * co2)
