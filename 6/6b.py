import sys

grid = [line.strip() for line in sys.stdin]

n, m = len(grid), len(grid[0])

x, y, d = -1, -1, -1
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

direction_map = {"^": 0, ">": 1, "v": 2, "<": 3}

for i in range(n):
    for j in range(m):
        if grid[i][j] in "^<>v":
            x = i
            y = j
            d = direction_map[grid[i][j]]
ans = 0
for i in range(n):
    for j in range(m):
        cx, cy, curr_d = x, y, d
        visited = [[[0] * 4 for i in range(m)] for j in range(n)]
        loop = False
        while 0 <= cx < n and 0 <= cy < m:
            if i == 9 and j == 7:
                print(cx, cy, curr_d)
            dx, dy = directions[curr_d]
            if 0 <= cx + dx < n and 0 <= cy + dy < m:
                while grid[cx + dx][cy + dy] == '#' or (cx + dx == i and cy + dy == j):
                    curr_d = (curr_d + 1) % 4
                    dx, dy = directions[curr_d]
                if visited[cx + dx][cy + dy][curr_d]:
                    loop = True
                    break
                visited[cx + dx][cy + dy][curr_d] = 1
                cx += dx
                cy += dy
            else:
                break
        ans += loop

print(ans)
