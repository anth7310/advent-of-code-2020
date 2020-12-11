
# https://adventofcode.com/2020/day/5

# part 1 - find unique ids 
max_id = 0
ids = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        # 128 rows, 8 columns
        row = list(range(0, 128))
        col = list(range(0, 8))
        line = line.strip()
        n_row = 128
        n_col = 8
        for c in line:
            if c == 'F': # lower half
                n_row //= 2
                row = row[:n_row]
            elif c == 'L':
                n_col //= 2
                col = col[:n_col]
            elif c == 'B':
                n_row //= 2
                row = row[n_row:]
            elif c == 'R':
                n_col //= 2
                col = col[n_col:]
        ids.append(row[0]*8 + col[0])
        max_id = max(ids[-1], max_id)
    print(max_id)

# part 2 - print missing number
v= []
ids.sort()
start = ids.pop(0)
while ids:
    nxt = ids.pop(0)
    if start + 1 != nxt:
        v.append(start + 1)
    start = nxt
print(v)