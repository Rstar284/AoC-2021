import collections
import itertools


def get_grid_from_lines(lines):
    for x, l in enumerate(lines):
        for y, v in enumerate(l.strip()):
            yield (x, y), int(v)


def get_grid_from_file(file_path="input"):
    with open(file_path) as f:
        return dict(get_grid_from_lines(f))


def show_grid(grid):
    x_vals = [x for x, _ in grid.keys()]
    y_vals = [y for _, y in grid.keys()]
    x_range = list(range(min(x_vals), 1 + max(x_vals)))
    y_range = list(range(min(y_vals), 1 + max(y_vals)))
    for x in x_range:
        print("".join(str(grid.get((x, y), "?")) for y in y_range))


def neighbours(p):
    x, y = p
    for dx, dy in itertools.product([-1, 0, 1], repeat=2):
        if (dx, dy) != (0, 0):
            yield x + dx, y + dy


def next_step(grid):
    grid2 = {p: v + 1 for p, v in grid.items()}
    to_flash = collections.deque([p for p, v in grid2.items() if v > 9])
    flashed = set()
    while to_flash:
        p = to_flash.popleft()
        if p not in flashed:
            flashed.add(p)
            for n in neighbours(p):
                if n in grid2:
                    grid2[n] += 1
                    if grid2[n] > 9:
                        to_flash.append(n)
    for p in flashed:
        grid2[p] = 0
    return grid2


def next_steps(grid, n):
    nb_flash = 0
    for i in range(n):
        grid = next_step(grid)
        nb_flash += sum(v == 0 for v in grid.values())
    return nb_flash


def first_synchro(grid):
    for i in itertools.count():
        if all(v == 0 for v in grid.values()):
            return i
        grid = next_step(grid)

if __name__ == "__main__":
    grid = get_grid_from_file()
    print(next_steps(grid, 100))
    print(first_synchro(grid))