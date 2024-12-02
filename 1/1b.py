import sys
from collections import defaultdict

left = []
right = defaultdict(int)

for line in sys.stdin:
    a, b = map(int, line.strip().split())
    left.append(a)
    right[b] += 1

print(sum([val * right[val] for val in left]))
    