import os
from itertools import combinations


def get_input(filename):
    with open(filename) as le_file:
        return le_file.read()


report_str = get_input(f'{os.path.dirname(__file__)}/input.txt')

report = [int(r) for r in report_str.split()]

for comb in combinations(report, 3):
    s = sum(comb)
    a, b, c = comb
    if s == 2020:
        print(a, b, c, a * b * c)
        break
