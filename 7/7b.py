import sys

res = 0

for line in sys.stdin:
    left, right = line.strip().split(": ")
    left = int(left)
    right = [*map(int, right.strip().split())]
    valid = False
    operators = len(right) - 1
    for i in range(3 ** operators):
        curr = right[0]
        for j in range(operators):
            bit = (i // (3 ** j)) % 3
            if bit == 0:
                curr += right[j + 1]
            elif bit == 1:
                curr *= right[j + 1]
            else:
                curr = int(str(curr) + str(right[j + 1]))
            if curr > left:
                break
        if curr == left:
            valid = True
            break
    if valid: res += left

print(res)
