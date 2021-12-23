import re
from collections import defaultdict, Counter

def rotate(x, y, z, axis):
    if axis == 'x':
        return(x, -z, y)
    elif axis == 'y':
        return(-z, y, x)
    elif axis == 'z':
        return(-y, x, z)

def loc(x, y , z, n):
    return (
        (x, y, z),
        (-y, x, z),
        (-x, -y, z),
        (y, -x, z),
        (-z, y, x),
        (-y, -z, x),
        (z, -y, x),
        (y, z, x),
        (-x, y, -z),
        (-y, -x, -z),
        (x, -y, -z),
        (y, x, -z),
        (z, y, -x),
        (-y, z, -x),
        (-z, -y, -x),
        (y, -z, -x),
        (x, -z, y),
        (z, x, y),
        (-x, z, y),
        (-z, -x, y),
        (x, z, -y),
        (-z, x, -y),
        (-x, -z, -y),
        (z, -x, -y),
    )[n]


def common_points(s1, s2, offset):
    c = 0
    for p in s2:
        p = tuple(p[i] + offset[i] for i in range(3))
        if p in s1:
            c += 1
    return c

def match(s1, s2):
    for var in range(24):
        s2a = set(loc(*p, var) for p in s2)
        c = Counter()
        for p1 in s1:
            for p2 in s2a:
                offset = tuple(p1[i] - p2[i] for i in range(3))
                c[offset] += 1
        offset, cnt = c.most_common()[0]
        if cnt >= 12:
            return var, offset
    return None

def run():
    input = open('input', 'r')
    scanners = []
    cur_sc = None
    for line in input:
        line = line.strip()
        if m := re.search(r'scanner (\d+)', line):
            cur_sc = set()
            scanners.append(cur_sc)
        elif line == '':
            pass
        else:
            cur_sc.add(tuple(int(n) for n in line.split(',')))

    sea = scanners.pop()
    offs = []
    while scanners:
        for sc in scanners:
            if r := match(sea, sc):
                var, offset = r
                offs.append(offset)
                for p in sc:
                    p = loc(*p, var)
                    p = tuple(p[i] + offset[i] for i in range(3))
                    sea.add(p)
                scanners = [s for s in scanners if s != sc]
                break

    print(len(sea))

    dists = []
    for s1 in offs:
        for s2 in offs:
            dists.append(sum(abs(s1[i]-s2[i]) for i in range(3)))
    print(max(dists))

run()