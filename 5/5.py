import sys
from collections import deque, defaultdict

orders = set()
rows = []

for line in sys.stdin:
    if line.strip() == "": continue
    if "|" in line:
        a, b = map(int, line.strip().split("|"))
        orders.add((a, b))
    else:
        rows.append([*map(int, line.strip().split(","))])

ans1, ans2 = 0, 0
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
        ans1 += row[len(row) // 2] 
    else:
        graph = defaultdict(list)
        indegrees = [0] * len(row)
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if (row[i], row[j]) in orders:
                    graph[i].append(j)
                    indegrees[j] += 1
                if (row[j], row[i]) in orders:
                    graph[j].append(i)
                    indegrees[i] += 1
        q = deque([])
        for i in range(len(row)):
            if indegrees[i] == 0:
                q.append(i)
        toposorted = []
        while len(q) > 0:
            u = q.popleft()
            toposorted.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        ans2 += row[toposorted[len(row) // 2]]

print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")








        
        