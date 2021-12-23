import re
input = re.findall(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', open('input', 'r').read())
cubes = []

def get_command(line):
    oo, coords = line.split()
    m = re.match(r'x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', coords)
    return (oo == 'on', [int(x) for x in m.groups()])
commands = [get_command(line) for line in open('input', 'r').read().splitlines()]

on = set()
for is_on, bounds in commands:
    x1, x2, y1, y2, z1, z2 = bounds
    for x in range(max(-50, x1), min(51, x2 + 1)):
        for y in range(max(-50, y1), min(51, y2 + 1)):
            for z in range(max(-50, z1), min(51, z2 + 1)):
                if is_on:
                    on.add((x, y, z))
                else:
                    on.discard((x, y, z))
print(len(on))


for step in input:
    step = [int(x) if x.strip('-').isnumeric() else x for x in step]
    [op, ux, vx, uy, vy, uz, vz] = step
    for cubes_i in range(len(cubes)):
        [ux2, vx2, uy2, vy2, uz2, vz2] = cubes[cubes_i]
        if ux > vx2 or vx < ux2 or uy > vy2 or vy < uy2 or uz > vz2 or vz < uz2:
            continue
        cubes[cubes_i] = None
        if ux > ux2:
            cubes.append((ux2, ux - 1, uy2, vy2, uz2, vz2))
        if vx < vx2:
            cubes.append((vx + 1, vx2, uy2, vy2, uz2, vz2))
        if uy > uy2:
            cubes.append((max(ux2, ux), min(vx2, vx), uy2, uy - 1, uz2, vz2))
        if vy < vy2:
            cubes.append((max(ux2, ux), min(vx2, vx), vy + 1, vy2, uz2, vz2))
        if uz > uz2:
            cubes.append((max(ux2, ux), min(vx2, vx), max(uy2, uy), min(vy2, vy), uz2, uz - 1))
        if vz < vz2:
            cubes.append((max(ux2, ux), min(vx2, vx), max(uy2, uy), min(vy2, vy), vz + 1, vz2))
    if op == 'on':
        cubes.append((min(ux, vx), max(ux, vx), min(uy, vy), max(uy, vy), min(uz, vz), max(uz, vz)))
    cubes = [cube for cube in cubes if cube is not None]

on_count = 0
for cube in cubes:
    [ux, vx, uy, vy, uz, vz] = cube
    on_count += (vx - ux + 1) * (vy - uy + 1) * (vz - uz + 1)
print(on_count)