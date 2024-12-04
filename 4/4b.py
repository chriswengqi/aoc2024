import sys

grid = [line.strip() for line in sys.stdin]

n, m = len(grid), len(grid[0])

ans = 0

words = ['MAS','SAM']

for i in range(n - 2):
    for j in range(m - 2):
        left = f"{grid[i][j]}{grid[i + 1][j + 1]}{grid[i + 2][j + 2]}"
        right = f"{grid[i][j + 2]}{grid[i + 1][j + 1]}{grid[i + 2][j]}"
        ans += left in words and right in words

print(ans)




        