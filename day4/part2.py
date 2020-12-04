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


def validate_byr(byr):
    return byr.isdigit() and 1920 <= int(byr) <= 2002


def validate_iyr(iyr):
    return iyr.isdigit() and 2010 <= int(iyr) <= 2020


def validate_eyr(eyr):
    return eyr.isdigit() and 2020 <= int(eyr) <= 2030


def validate_hgt(hgt):
    number, units = hgt[:-2], hgt[-2:]
    if units not in ('cm', 'in'):
        return False
    if units == 'cm':
        return number.isdigit() and 150 <= int(number) <= 193
    if units == 'in':
        return number.isdigit() and 59 <= int(number) <= 76


def validate_hcl(hcl):
    return re.match(r'^#([0-9a-f]{6})$', hcl)


def validate_ecl(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_pid(pid):
    return re.match(r'^([0-9]{9})$', pid)


def validate(fields):
    return (
        validate_byr(fields.get('byr'))
        and validate_iyr(fields.get('iyr'))
        and validate_eyr(fields.get('eyr'))
        and validate_hgt(fields.get('hgt'))
        and validate_hcl(fields.get('hcl'))
        and validate_ecl(fields.get('ecl'))
        and validate_pid(fields.get('pid'))
    )


valid_amount = 0

for batch in batches:
    parts = re.split(r'\s+', batch)
    found_fields = {s[0]: s[1] for s in [p.split(':') for p in parts if p]}
    if required_fields.issubset(set(found_fields.keys())) and validate(found_fields):
        valid_amount += 1

print(valid_amount)
