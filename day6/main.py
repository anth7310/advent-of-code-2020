# day 6
# https://adventofcode.com/2020/day/6

# part 2
with open('input.txt', 'r') as f:
    dat = set()
    count = 0
    include = True
    # include last line as empty string
    for line in f.readlines() + ['']:
        line = line.strip()
        if line == '':
            count += len(dat)
            dat = set()
            include = True
        else:
            # init starting set
            if len(dat) == 0 and include:
                [ dat.add(v) for v in line ]
                include = False
            # find end intersecting set
            else:
                dat = dat.intersection([ v for v in line ])
    print(count)

