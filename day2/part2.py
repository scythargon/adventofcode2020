#!/usr/bin/env -S python

import os


def get_input(filename):
    with open(filename) as le_file:
        return le_file.read()


input_file = f'{os.path.dirname(__file__)}/input.txt'
input_data = get_input(input_file).split('\n')

correct_amount = 0

for line in input_data:
    policy, password = line.split(': ')
    _range, letter = policy.split()
    first_index, second_index = [int(t) for t in _range.split('-')]

    equalities = password[first_index - 1] == letter, password[second_index - 1] == letter

    if sum(equalities) == 1:
        correct_amount += 1

print(correct_amount)
