#!/usr/bin/env -S python
import os


def get_input(filename):
    with open(filename) as le_file:
        return le_file.read()


input_file = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
input_data = get_input(input_file).split('\n')

correct_amount = 0

for line in input_data:
    policy, password = line.split(': ')
    _range, letter = policy.split()
    lowest, highest = [int(t) for t in _range.split('-')]

    found_times = password.count(letter)
    if lowest <= found_times <= highest:
        correct_amount += 1

print(correct_amount)
