#!/usr/bin/env -S python
import re
from pathlib import Path


default_input_file = Path(__file__).parent.resolve() / "input.txt"


def get_input(filename=default_input_file):
    with open(filename) as le_file:
        return le_file.read()


input_data = get_input()

batches = input_data.split('\n\n')

required_fields = {
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    # 'cid',  # (Country ID)
}

valid_amount = 0
for batch in batches:
    parts = re.split(r'\s+', batch)
    found_fields = set([p.split(':')[0] for p in parts if p])
    if required_fields.issubset(found_fields):
        valid_amount += 1

print(valid_amount)
