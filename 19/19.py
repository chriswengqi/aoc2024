import sys
from functools import cache

patterns = set()

@cache
def dfs(curr, string):
    if curr == len(string):
        return 1
    ans = 0
    for i in range(curr + 1, len(string) + 1):
        if string[curr: i] in patterns:
            ans += dfs(i, string)
    return ans

ans1, ans2 = 0, 0

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    if "," in line:
        for pattern in line.split(", "):
            patterns.add(pattern)
    else:
        res = dfs(0, line)
        ans1 += res > 0
        ans2 += res
print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")


        
