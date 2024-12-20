import sys
from collections import deque
grid = [line.strip() for line in sys.stdin]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = len(grid), len(grid[0])
si, sj, ei, ej = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            si, sj = i, j
        if grid[i][j] == 'E':
            ei, ej = i, j

sp_from_s = [[-1] * m for _ in range(n)]
sp_from_e = [[-1] * m for _ in range(n)]

def dijsktra(x, y, sp):
    q = deque([])
    q.append(((x, y), 0))
    sp[x][y] = 0

    while len(q) > 0:
        (x, y), dist = q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 1 <= nx < n - 1 and 1 <= ny < m - 1 and grid[nx][ny] != '#' and sp[nx][ny] == -1:
                sp[nx][ny] = dist + 1
                q.append(((nx, ny), dist + 1))


dijsktra(si, sj, sp_from_s)
dijsktra(ei, ej, sp_from_e)

res = sp_from_s[ei][ej]

def run(val):
    ans = 0
    for i in range(n):
        for j in range(m):
            for k in range(max(0, i - val), min(n, i + val + 1)):
                for l in range(max(0, j - val), min(m, j + val + 1)):
                    cheat_distance = abs(i - k) + abs(j - l)
                    if grid[i][j] == '#' or grid[k][l] == '#' or cheat_distance > val:
                        continue
                    diff = sp_from_s[i][j] + sp_from_e[k][l] + cheat_distance
                    ans += diff <= res - 100
    return ans



print(f"Part 1: {run(2)}")
print(f"Part 2: {run(20)}")

        
