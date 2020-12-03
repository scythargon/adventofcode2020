#!/usr/bin/env -S python
import os
from functools import reduce


def get_input(filename):
    with open(filename) as le_file:
        return le_file.read()


input_file = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
slope_map = get_input(input_file).splitlines()
map_width = len(slope_map[0])
finish_y = len(slope_map)


def count_trees(dx, dy):
    trees_hit = 0

    x, y = 0, 0

    while y != finish_y - 1:
        x += dx
        y += dy
        whatsthere = slope_map[y][x % map_width]
        if whatsthere == '#':
            trees_hit += 1

    return trees_hit


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

hits = [count_trees(*slope) for slope in slopes]
print(hits)

print(reduce(lambda x, y: x * y, hits))
