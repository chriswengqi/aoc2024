import sys

left, right = [], []

for line in sys.stdin:
    a, b = map(int, line.strip().split())
    left.append(a)
    right.append(b)

left.sort()
right.sort()

print(sum([abs(left[i] - right[i]) for i in range(len(left))]))