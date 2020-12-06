# day 4
# https://adventofcode.com/2020/day/4
with open('input.txt', 'r') as f:
    count = 0
    passport = dict()
    # read batch input seperated by blank line
    for line in f.readlines():
        line = line.strip()
        if line == '':
            if set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) == (set(passport) - set(['cid'])):
                count += 1
            passport = dict()
        else:
            for word in line.split():
                key, value = word.split(':')
                passport[key] = value
    # read last batch since last newline in file doesn't equal ''
    if set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) == (set(passport) - set(['cid'])):
                count += 1
    print(count)

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def check_passport(passport):
    """ Return True if passport meets requirements
    """
    valid = True
    if not (1920 <= int(passport['byr']) <= 2002):
        valid = False
    if not (2010 <= int(passport['iyr']) <= 2020):
        valid = False
    if not (2020 <= int(passport['eyr']) <= 2030):
        valid = False
    if passport['hgt'].endswith('cm'):
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            valid = False
    if passport['hgt'].endswith('in'):
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            valid = False
    hcl = passport['hcl']
    if not (hcl.startswith('#') and len(hcl) == 7 and hcl[1:].isalnum() and hcl.lower() == hcl):
        for v in hcl[1:]:
            if v.isalpha():
                if not v in 'abcdef':
                    valid = False
    if not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        valid = False
    if not (passport['pid'].isnumeric() and len(passport['pid']) == 9):
        valid = False
    return valid

# part 2
with open('input.txt', 'r') as f:
    count = 0
    passport = dict()
    # read batch input seperated by blank line
    for line in f.readlines():
        line = line.strip()
        if line == '':
            if set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) == (set(passport) - set(['cid'])):
                if check_passport(passport):
                    count += 1
            passport = dict()
        else:
            for word in line.split():
                key, value = word.split(':')
                passport[key] = value
    # read last batch since last newline in file doesn't equal ''
    if set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) == (set(passport) - set(['cid'])):
        if check_passport(passport):
            count += 1
    print(count)
