#!/usr/bin/env -S python
import os


def get_input(filename):
    with open(filename) as le_file:
        return le_file.read()


input_file = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
slope_map = get_input(input_file).splitlines()
map_width = len(slope_map[0])

trees_hit = 0

x, y = 0, 0
dx, dy = 3, 1


finish_y = len(slope_map)

while y != finish_y - 1:
    x += dx
    y += dy
    whatsthere = slope_map[y][x % map_width]
    if whatsthere == '#':
        trees_hit += 1


print(trees_hit)
