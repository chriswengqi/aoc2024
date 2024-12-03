import sys
import re

ans = 0

pattern = r"mul\((-?\d+),(-?\d+)\)|do\(\)|don't\(\)"

enabled = True

for line in sys.stdin:
    matches = re.finditer(pattern, line)

    for match in matches:
        if match.group(1): 
            ans += int(match.group(1)) * int(match.group(2)) if enabled else 0
        else:
            enabled = match.group(0) == 'do()'

print(ans)
        
        
        