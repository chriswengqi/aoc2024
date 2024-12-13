import sys
from collections import defaultdict

left, right_lst, right_dic = [], [], defaultdict(int)

for line in sys.stdin:
    a, b = map(int, line.strip().split())
    left.append(a)
    right_lst.append(b)
    right_dic[b] += 1

left.sort()
right_lst.sort()

print(f"Part 1: {sum([abs(left[i] - right_lst[i]) for i in range(len(left))])}")
print(f"Part 2: {sum([val * right_dic[val] for val in left])}")