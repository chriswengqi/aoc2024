import sys
from collections import deque

sz = 71
grid = [['.'] * sz for _ in range(sz)] 
DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
coordinates = []
ctr = 0

class DSU:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

def part1():
    q = deque([])
    q.append(((0, 0), 0))
    visited = [[0] * sz for _ in range(sz)]
    visited[0][0] = 1
    while len(q) > 0:
        (x, y), dist = q.popleft()
        if x == sz - 1 and y == sz - 1:
            return dist
        for dx, dy in DIRS:
            if 0 <= x + dx < sz and 0 <= y + dy < sz and grid[x + dx][y + dy] != '#' and not visited[x + dx][y + dy]:
                visited[x + dx][y + dy] = 1
                q.append(((x + dx, y + dy), dist + 1)) 

def part2():
    visited = [[0] * sz for _ in range(sz)]
    dsu = DSU(sz * sz)

    for i in range(sz):
        for j in range(sz):
            if not visited[i][j]:
                q = deque([])
                q.append((i, j))
                visited[i][j] = 1
                while len(q) > 0:
                    x, y = q.popleft()
                    for dx, dy in DIRS:
                        if 0 <= x + dx < sz and 0 <= y + dy < sz and grid[x + dx][y + dy] != '#' and not visited[x + dx][y + dy]:
                            q.append((x + dx, y + dy))
                            visited[x + dx][y + dy] = 1
                            dsu.union(i * sz + j, (x + dx) * sz + y + dy)

    for x, y in coordinates[::-1]:
        grid[x][y] = '.'
        for dx, dy in DIRS:
            if 0 <= x + dx < sz and 0 <= y + dy < sz and grid[x + dx][y + dy] == '.':
                dsu.union(x * sz + y, (x + dx) * sz + y + dy)
        
        if dsu.find(0) == dsu.find(sz * sz - 1):
            return f"{x},{y}"

for line in sys.stdin:
    x, y = map(int, line.strip().split(","))
    grid[x][y] = '#'
    coordinates.append((x, y))
    ctr += 1
    if ctr == 1024:
        print(f"Part 1: {part1()}")

print(f"Part 2: {part2()}")
