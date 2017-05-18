#!/usr/bin/python3
# Generate a random convex polygon using Valtr's algorithm
import sys
import math
import random

def random_partition(a):
    b = list()
    c = list()
    for i in range(len(a)):
        if random.randrange(2):
            b.append(a[i])
        else:
            c.append(a[i])
    return b, c

def get_deltas(n):
    de = [random.random() for _ in range(n)]
    de.sort()
    dep, dem = random_partition(de[1:-1])
    dem.reverse()
    des = [de[0]] + dep + [de[-1]] + dem + [de[0]]
    deltas = [des[i] - des[i-1] for i in range(1, len(des))]
    return deltas, (de[0], de[-1])

def get_xyq(n):
    x, (a1, a2) = get_deltas(n)
    y, (b1, b2) = get_deltas(n)
    random.shuffle(y)
    vectors = [(x[i], y[i]) for i in range(n)]
    vectors.sort(key=lambda v: math.atan2(v[1], v[0]))
    points = [(0, 0)]
    for v in vectors:
        points.append((points[-1][0] + v[0], points[-1][1] + v[1]))
    xmin = min([p[0] for p in points])
    ymin = min([p[1] for p in points])
    dx = a1 - xmin
    dy = b1 - ymin
    points = [(p[0]+dx, p[1]+dy) for p in points]
    return points


import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = 20
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    points = get_xyq(n)
    plt.plot([p[0] for p in points], [p[1] for p in points])
    plt.ylabel('some numbers')
    plt.show()
