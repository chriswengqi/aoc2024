import sys

grid = [line.strip() for line in sys.stdin]
n, m = len(grid), len(grid[0])
dic = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            if grid[i][j] not in dic:
                dic[grid[i][j]] = []
            dic[grid[i][j]].append((i, j))

s = set()

for k, v in dic.items():
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            dx, dy = v[i][0] - v[j][0], v[i][1] - v[j][1]
            x1, y1 = v[i][0] + dx, v[i][1] + dy
            x2, y2 = v[j][0] - dx, v[j][1] - dy
            if 0 <= x1 < n and 0 <= y1 < m:
                s.add((x1, y1))
            if 0 <= x2 < n and 0 <= y2 < m:
                s.add((x2, y2))

print(len(s))