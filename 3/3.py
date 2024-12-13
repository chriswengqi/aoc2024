import sys
import re

ans1, ans2 = 0, 0

pattern1 = r"mul\((-?\d+),(-?\d+)\)"
pattern2 = r"mul\((-?\d+),(-?\d+)\)|do\(\)|don't\(\)"
enabled = True
for line in sys.stdin:
    matches1 = re.findall(pattern1, line)
    matches2 = re.finditer(pattern2, line)
    for x, y in matches1:
        ans1 += int(x) * int(y)

    for match in matches2:
        if match.group(1): 
            ans2 += int(match.group(1)) * int(match.group(2)) if enabled else 0
        else:
            enabled = match.group(0) == 'do()'

print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")



        