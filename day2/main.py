# part 1
# https://adventofcode.com/2020/day/2
# with open('input_1.txt', 'r') as f:
#     count = 0
#     for line in f.readlines():
#         a, b, c = line.split()
#         min_count, max_count = [int(i) for i in a.split('-')]
#         letter = b[0]
#         word = c

#         if min_count <= word.count(letter) <= max_count:
#             count += 1
# print(count)

# part 2
with open('input.txt', 'r') as f:
    count = 0
    for line in f.readlines():
        a, b, c = line.split()
        min_count, max_count = [int(i) for i in a.split('-')]
        letter = b[0]
        word = c

        if "".join([word[min_count-1], word[max_count-1]]).count(letter) == 1:
            count += 1
print(count)