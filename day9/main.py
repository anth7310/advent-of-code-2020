
def two_sum_dict(arr, k):
    c = {}
    for num in arr:
        if k in arr:
            return True
        comp = k - num
        c[comp] = num
    return False

# part 1
nums = []
with open('day9_input.txt', 'r') as f:
    for line in f.readlines():
        nums.append(int(line))


def two_sum_bubble(arr, k):
    for i1, v1 in enumerate(arr):
        for i2, v2 in enumerate(arr):
            if v1 + v2 == k:
                return True
    return False

for i in range(0, len(nums)-25):
    # find sum of previous 25 nums, check if exist
    exist = two_sum_bubble(nums[i:i+25], nums[i+25])

    if not exist:
        c = nums[i+25]
        print(nums[i+25], i)
        break

# part 2
for i1 in range(len(nums[:i+25])):
    for i2 in range(i1, len(nums[:i+25])):
        if sum(nums[i1:i2]) == c:
            print(min(nums[i1:i2]) + max(nums[i1:i2]))            

