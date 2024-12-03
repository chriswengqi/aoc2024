import sys
import re

ans = 0

pattern = r"mul\((-?\d+),(-?\d+)\)"
for line in sys.stdin:
    matches = re.findall(pattern, line)
    for x, y in matches:
        ans += int(x) * int(y)

print(ans)



        