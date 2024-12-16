import sys
from heapq import *

grid  = [line.strip() for line in sys.stdin]
n, m = len(grid), len(grid[0])
INF = 1000000000
sx, sy, ex, ey = -1, -1, -1, -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            sx, sy = i, j
        if grid[i][j] == 'E':
            ex, ey = i, j

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dijkstra(start, ex, ey):
    q = []
    for sx, sy, d in start:
        heappush(q, (0, sx, sy, d))
    D = {}
    sp = INF
    while len(q) > 0:
        dist, x, y, d = heappop(q)
        if (x, y, d) in D:
            continue
        D[(x, y, d)] = dist
        if x == ex and y == ey:
            sp = min(dist, sp)
        dx, dy = directions[d]
        if grid[x + dx][y + dy] != "#":
            heappush(q, (dist + 1, x + dx, y + dy, d))
        heappush(q, (dist + 1000, x, y, (d - 1) % 4))
        heappush(q, (dist + 1000, x, y, (d + 1) % 4))

    return D, sp

A, sp = dijkstra([(sx, sy, 0)], ex, ey)
B, _ = dijkstra([(ex, ey, i) for i in range(4)], sx, sy)
res = set()
for x, y, d in B:
    if B[(x, y, d)] + A.get((x, y, (d + 2) % 4), INF) == sp:
        res.add((x, y))
print(f"Part 1: {sp}")
print(f"Part 2: {len(res)}")









