from collections import Counter

def day06(input):
    nums = map(int, input.strip().split(','))

    population = Counter(nums)

    for day in range(256):
        for old_age in range(9):
            population[old_age - 1] = population[old_age]
            population[old_age] = 0
        birth_count = population[-1]
        del population[-1]
        population[6] += birth_count
        population[8] = birth_count
        if day == 79:
            population_part1 = population.copy()

    part1 = sum(population_part1.values())
    part2 = sum(population.values())

    return part1, part2

if __name__ == "__main__":
    input = open('input.txt').read()
    print(*day06(input))