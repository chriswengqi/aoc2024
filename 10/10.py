import sys

grid = [line.strip() for line in sys.stdin]
n, m = len(grid), len(grid[0])
s = set()

DIRS = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def dfs(x, y, curr):
    if curr == 9:
        s.add((x, y))
        return 1
    ans = 0
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and str(curr + 1) == grid[nx][ny]:
            ans += dfs(nx, ny, curr + 1)
    return ans

a1, a2 = 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            a2 += dfs(i, j, 0)
            a1 += len(s)
            s.clear()

print(f"Part 1: {a1}")
print(f"Part 2: {a2}")