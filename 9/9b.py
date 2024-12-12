import sys
from collections import deque

s = ""
for line in sys.stdin:
    s = line.strip()
start = 0
val = 0
segments = []
spaces = []
new_segments = {}

for i, elem in enumerate(s):
    if i % 2 == 0:
        segments.append((val, start, int(elem)))
        new_segments[val] = (start, int(elem))
        val += 1
    else:
        spaces.append((start, int(elem)))
    start += int(elem)

for val, seg_start, seg_sz in segments[::-1]:
    for i, (space_start, space_sz) in enumerate(spaces):
        if seg_sz <= space_sz:
            new_segments[val] = (space_start, seg_sz)
            spaces[i] = (space_start + seg_sz, space_sz - seg_sz)
            break
        if seg_start <= space_start:
            break
ans = 0
for k, (start, sz) in new_segments.items():
    for val in range(start, start + sz):
        ans += val * k

print(ans)




