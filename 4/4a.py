import sys

grid = [line.strip() for line in sys.stdin]

n, m = len(grid), len(grid[0])
directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
word = 'XMAS'

def search(idx, x, y, dx, dy):
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != word[idx]:
        return 0
    return 1 if idx == 3 else search(idx + 1, x + dx, y + dy, dx, dy)

ans = 0

for i in range(n):
    for j in range(m):
        for dx, dy in directions:
            ans += search(0, i, j, dx, dy)

print(ans)
            
        
        