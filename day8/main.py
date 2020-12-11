
# read commands into a list
commands = []
with open('input.txt', 'r') as f:
    # store values in commands list
    for line in f.readlines():
        commands.append(line.strip())
# part 1
acc = 0
# store state if being run a second time
ht = [0]*len(commands)
i = 0
while True:
    ins, v = commands[i].split()
    v = int(v)
    if ht[i]: # command already run
        print(acc)
        break
    ht[i] = 1
    if ins == 'acc':
        acc += v
        i += 1
    elif ins == 'jmp':
        i += v
    elif ins == 'nop':
        i += 1

# part 2, change exactly one jmp (to nop) or nop (to jmp)
acc = 0
# store state if being run a second time
ht = [0]*len(commands)
def f(i, ht, acc, commands, first=True):

    while i < len(ht):
        ins, v = commands[i].split()
        v = int(v)
        if ht[i]: # command already run
            return False
        ht[i] = 1
        if ins == 'acc':
            acc += v
            i += 1
        elif ins == 'jmp':
            if first:
                c = commands[:]
                c[i] = 'nop %i' % v
                i += 1
                f(i, ht[:], acc, c, False)
            else:
                i += v

        elif ins == 'nop':
            if first:
                c = commands[:]
                c[i] = 'jmp %i' % v
                i += v
                f(i, ht[:], acc, c, False)
            else:
                i += 1

    print(acc, len(ht), i)
    # exit()
    return True

f(0, ht, 0, commands)