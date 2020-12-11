# https://adventofcode.com/2020/day/7

# part 1
d = {} # child references parent
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip() # remove new line
        parent, child = line.split('contain')
        parent = parent.strip()
        child = child.strip()

        p = ' '.join(parent.split()[0:2])
        if child == 'no other bags.':
            d[p] = None
        else:
            i, j = 1, 2
            children = child.split()
            while j < len(children):
                c = ' '.join([children[i], children[j]])
                d.update({c: d.get(c, [])})
                if d.get(c) != None:
                    d[c].append(p)
                i += 4
                j += 4

frontier = d['shiny gold']
bags = set()
while frontier:
    b = frontier.pop()
    bags.add(b)
    if b in d:
        frontier += [b_ for b_ in d[b] if b_ not in bags]

print(len(bags))