import sys
grid1, grid2 = [], []
to_grid = True
movements = ""
mapped_tiles = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
for line in sys.stdin:
    if line.strip() == "":
        to_grid = False
        continue
    if to_grid:
        row = []
        for tile in line.strip():
            row.extend(mapped_tiles[tile])
        grid1.append([*line.strip()])
        grid2.append(row)
    else:
        movements += line.strip()

n, m = len(grid1), len(grid1[0])
x, y = -1, -1

for i in range(n):
    for j in range(m):
        if grid1[i][j] == '@':
            x, y = i, j

directions = {"<": [0, -1], ">": [0, 1], "v": [1, 0], "^": [-1, 0]}

def is_valid_push(xs, ys, dx, dy, grid, prev_s):
    s = set()
    for x, y in zip(xs, ys):
        if grid[x + dx][y + dy] == "#":
            return False
        elif grid[x + dx][y + dy] == "[":
            s.add((x + dx, y + dy))
            s.add((x + dx, y + dy + 1))
        elif grid[x + dx][y + dy] == "]":
            s.add((x + dx, y + dy))
            s.add((x + dx, y + dy - 1))
    if len(s) == 0:
        return True
    else:
        xs, ys = [], []
        for x, y in s:
            prev_s.add((x, y))
            xs.append(x)
            ys.append(y)
        return is_valid_push(xs, ys, dx, dy, grid, prev_s)

def simulate_part_1(x, y, grid, char):
    dx, dy = directions[char]
    nx, ny = x + dx, y + dy
    while grid[nx][ny] == "O":
        nx += dx
        ny += dy
    if grid[nx][ny] == ".":
        if nx == x + dx and ny == y + dy:
            grid[nx][ny], grid[x][y] = grid[x][y], grid[nx][ny]
        else:
            grid[x][y] = "."
            grid[x + dx][y + dy] = "@"
            grid[nx][ny] = "O"
        x, y = x + dx, y + dy
    return x, y

def simulate_part_2(x, y, grid, char):
    dx, dy = directions[char]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == ".":
        grid[nx][ny], grid[x][y] = grid[x][y], grid[nx][ny]
        x, y = nx, ny
    elif grid[nx][ny] in "[]" and char in "<>":
        while grid[nx][ny] in "[]":
            nx += dx
            ny += dy
        if grid[nx][ny] != "#":
            while nx != x or ny != y:
                grid[nx][ny] = grid[nx - dx][ny - dy]
                nx -= dx
                ny -= dy
            grid[x][y] = "."
            x, y = x + dx, y + dy
    elif grid[nx][ny] in "[]":
        s = set()
        if is_valid_push([x], [y], dx, dy, grid, s):
            sorted = {}
            for r, c in s:
                if r not in sorted:
                    sorted[r] = []
                sorted[r].append(c)
            arr = []
            for k, v in sorted.items():
                arr.append((k, v))
            arr.sort()
            if char == "^":
                for r, cs in arr:
                    for c in cs:
                        grid[r - 1][c], grid[r][c] = grid[r][c], grid[r - 1][c]
            else:
                for r, cs in arr[::-1]:
                    for c in cs:
                        grid[r + 1][c], grid[r][c] = grid[r][c], grid[r + 1][c]
            grid[x + dx][y + dy], grid[x][y] = grid[x][y], grid[x + dx][y + dy]
            x, y = nx, ny
    return x, y

def calculate_ans(grid, char):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                ans += 100 * i + j
    return ans

x1, y1, x2, y2 = x, y, x, y * 2

for char in movements:
    x1, y1 = simulate_part_1(x1, y1, grid1, char)
    x2, y2 = simulate_part_2(x2, y2, grid2, char)


print(f"Part 1: {calculate_ans(grid1, 'O')}")
print(f"Part 2: {calculate_ans(grid2, '[')}")              

