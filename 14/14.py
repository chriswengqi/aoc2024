import sys
from time import sleep

a, b, c, d = 0, 0, 0, 0

arr = []

for line in sys.stdin:
    p, v = line.strip().split()
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))

    final_x = (px + vx * 100) % 101
    final_y = (py + vy * 100) % 103

    a += final_x <= 49 and final_y <= 50
    b += final_x > 50 and final_y <= 50
    c += final_x <= 49 and final_y > 51
    d += final_x > 50 and final_y > 51

    arr.append((px, py, vx, vy))

adj_score = []

for i in range(10000):
    togetherness = 0
    dic = {}
    mx = -1
    mx_idx = -1

    for px, py, vx, vy in arr:
        x = (px + vx * i) % 101
        y = (py + vy * i) % 103
        if y not in dic:
            dic[y] = []
        dic[y].append(x)

    for k, v in dic.items():
        v.sort()
        for j in range(1, len(v)):
            if v[j] == v[j - 1] + 1:
                togetherness += 1

    adj_score.append((togetherness, i))


adj_score.sort(reverse=True)
ANS = adj_score[0][1]

print(f"Part 1: {a * b * c * d}")
print(f"Part 2: {ANS}")

grid = [[' '] * 101 for _ in range(103)]

for px, py, vx, vy in arr:
    x = (px + vx * ANS) % 101
    y = (py + vy * ANS) % 103
    grid[y][x] = '*'

for line in grid:
    print("".join(line))


