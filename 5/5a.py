import sys
from collections import deque

orders = set()
rows = []

for line in sys.stdin:
    if line.strip() == "": continue
    if "|" in line:
        a, b = map(int, line.strip().split("|"))
        orders.add((a, b))
    
    else:
        rows.append([*map(int, line.strip().split(","))])

ans = 0
for row in rows:
    valid = True
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if (row[j], row[i]) in orders:
                valid = False
                break
        if not valid:
            break
    if valid:
        ans += row[len(row) // 2] 
print(ans)








        
        