import sys
from collections import defaultdict, deque

grid = [line.strip() for line in sys.stdin]
n, m = len(grid), len(grid[0])
visited = [[0] * m for _ in range(n)]
DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
next_edge = [((0, 1, 0), (0, 0, 1), (-1, 1, 3)), ((1, 0, 1), (0, 0, 2), (1, 1, 0)), ((0, -1, 2), (0, 0, 3), (1, -1, 1)), ((-1, 0, 3), (0, 0, 0), (-1, -1, 2))]

a1, a2 = 0, 0

def count_sides(curr, visited_sides, partitions):
    sides = 0
    while not visited_sides[curr]:
        visited_sides[curr] = 1
        x, y, dir = curr
        same_side = False
        for dx, dy, new_dir in next_edge[dir]:
            if (x + dx, y + dy, new_dir) in partitions:
                curr = (x + dx, y + dy, new_dir)
                if new_dir != dir:
                    sides += 1
                break

    return sides

for i in range(n):
    for j in range(m):
        if visited[i][j]: continue
        q, s = deque([]), set()
        s = set()
        area, sides = 0, 0
        q.append((i, j))
        s.add((i, j))
        visited[i][j] = 1
        while len(q) > 0:
            x, y = q.popleft()
            area += 1
            for dx, dy in DIRS:
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x][y] == grid[x + dx][y + dy] and not visited[x + dx][y + dy]:
                    q.append((x + dx, y + dy))
                    s.add((x + dx, y + dy))
                    visited[x + dx][y + dy] = 1
        partitions, visited_sides = set(), {}
        perimeter = area * 4
        for x, y in s:
            for idx, (dx, dy) in enumerate(DIRS):
                if not (0 <= x + dx < n and 0 <= y + dy < m) or grid[x][y] != grid[x + dx][y + dy]:
                    partitions.add((x, y, idx))
                    visited_sides[(x, y, idx)] = 0
                if (x + dx, y + dy) in s:
                        perimeter -= 1

        for k in visited_sides:
            if not visited_sides[k]:
                sides += count_sides(k, visited_sides, partitions)
                    
        a1 += area * perimeter
        a2 += area * sides

print(f"Part 1: {a1}")
print(f"Part 2: {a2}")



