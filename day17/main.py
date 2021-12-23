def solve(data, part=2):
    words = data.split(" ")
    x = words[2][2:-1].split("..")
    y = words[3][2:].split("..")
    coords = ((int(x[0]), int(y[0])), (int(x[1]), int(y[1])))
    if part == 1:
        return part_one(*coords)
    elif part == 2:
        return part_two(*coords)


def part_one(low, high):
    return (-low[1] - 1) * -low[1] // 2


def part_two(low, high):
    combo = 0
    for x in range(high[0] + 1):
        for y in range(low[1], -low[1]):
            speed_x = x
            speed_y = y
            pos = (0, 0)
            while pos[0] <= high[0] and pos[1] >= low[1]:
                if pos[0] >= low[0] and pos[1] <= high[1]:
                    combo += 1
                    break

                pos = (pos[0] + speed_x, pos[1] + speed_y)
                if speed_x > 0:
                    speed_x -= 1
                speed_y -= 1

    return combo


if __name__ == "__main__":
	print(solve(open("input").read(), part=1))
	print(solve(open("input").read()))