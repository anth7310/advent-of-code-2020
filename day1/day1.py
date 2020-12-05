import requests
# https://adventofcode.com/2020/day/1

DATA = './day1.txt'

data = []
for line in open(DATA, 'r').readlines():
    data.append(int(line))

data.sort()

# 2 sum solution for sorted array

p1 = 0
p2 = len(data)-1

total = 2020
curr_sum = data[p1] + data[p2]
while curr_sum != total:
    if curr_sum > total:
        p2 -= 1
    else:
        p1 += 1
    curr_sum = data[p1] + data[p2]

print(curr_sum, data[p1], data[p2], data[p1]*data[p2])