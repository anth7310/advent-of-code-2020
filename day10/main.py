
arr = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        arr.append(int(line))

arr.append(max(arr) + 3)
arr.append(0)

i = 1
arr.sort()
d = {
    1: 0,
    2: 0,
    3: 0
}
while i < len(arr):
    diff = arr[i] - arr[i-1]
    d[diff] += 1
    i += 1
print(d[1] * d[3])


# part 2
counts = [0] * len(arr)
counts[0] = 1
i = 1
while i < len(counts):
    n = len(list(filter(lambda x, curr=arr[i]: 1 <= (curr - x) <= 3, arr[max(0, i-3):i])))
    counts[i] = sum(counts[max(0, i-n):i])
    i += 1
print(counts[-1])