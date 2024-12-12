import sys

grid = [line.strip() for line in sys.stdin]

n, m = len(grid), len(grid[0])

x, y = -1, -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == '^':
            x = i
            y = j

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
visited = set()
curr_d = 0
ans = 0
while 0 <= x < n and 0 <= y < m:
    if (x, y) not in visited:
        ans += 1
    visited.add((x, y))
    dx, dy = directions[curr_d]
    if 0 <= x + dx < n and 0 <= y + dy < m:
        while grid[x + dx][y + dy] == '#':
            curr_d = (curr_d + 1) % 4
            dx, dy = directions[curr_d]
        x += dx
        y += dy
    else:
        break

print(ans)
