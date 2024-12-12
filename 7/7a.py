import sys

res = 0

for line in sys.stdin:
    left, right = line.strip().split(": ")
    left = int(left)
    right = [*map(int, right.strip().split())]
    valid = False
    operators = len(right) - 1
    for i in range((1 << operators)):
        curr = right[0]
        for j in range(operators):
            if ((1 << j)) & i:
                curr += right[j + 1]
            else:
                curr *= right[j + 1]
        if curr == left:
            valid = True
            break
    if valid: res += left

print(res)
