#!/usr/bin/env -S python
from pathlib import Path


default_input_file = Path(__file__).parent.resolve() / "input.txt"


def get_input(filename=default_input_file):
    with open(filename) as le_file:
        return le_file.read()


input_data = get_input().splitlines()


def scan_boarding_pass(boarding_pass):
    range = [0, 127]
    for char in boarding_pass[:7]:
        step = (range[1] - range[0]) // 2 + 1
        # print(range)
        if char == 'F':
            range = [range[0], range[1] - step]
        elif char == 'B':
            range = [range[0] + step, range[1]]

    row = range[0]
    range = [0, 7]
    for char in boarding_pass[7:]:
        step = (range[1] - range[0]) // 2 + 1
        # print(range)
        if char == 'L':
            range = [range[0], range[1] - step]
        elif char == 'R':
            range = [range[0] + step, range[1]]
    seat = range[0]

    return (row, seat)


result = scan_boarding_pass('FBFBBFFRLR')
assert result == (44, 5)


taken_seats = []

for boarding_pass in input_data:
    row, seat = scan_boarding_pass(boarding_pass)

    if row == 0 or row == 127:
        continue

    seat_id = row * 8 + seat
    taken_seats.append(seat_id)


taken_seats = sorted(taken_seats)

for i, seat1 in enumerate(taken_seats[:-2]):
    if taken_seats[i + 2] != seat1 + 2:
        print(seat1)
