import sys

grid = [line.strip() for line in sys.stdin]

n, m = len(grid), len(grid[0])
directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
word = 'XMAS'
words = words = ['MAS','SAM']
ans1, ans2 = 0, 0

def search(idx, x, y, dx, dy):
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != word[idx]:
        return 0
    return 1 if idx == 3 else search(idx + 1, x + dx, y + dy, dx, dy)

for i in range(n):
    for j in range(m):
        for dx, dy in directions:
            ans1 += search(0, i, j, dx, dy)
        if i < n - 2 and j < m - 2:
            left = f"{grid[i][j]}{grid[i + 1][j + 1]}{grid[i + 2][j + 2]}"
            right = f"{grid[i][j + 2]}{grid[i + 1][j + 1]}{grid[i + 2][j]}"
            ans2 += left in words and right in words


print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")
            
        
        