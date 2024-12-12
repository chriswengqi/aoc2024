import sys
from collections import defaultdict
arr = []
for line in sys.stdin:
    arr = [*map(int, line.strip().split())]

dic = {}

def f(x, y):
    if y == 0: return 1
    if (x, y) in dic: return dic[(x, y)]
    length = len(str(x)) 
    if x == 0:
        dic[(x, y)] = f(1, y - 1)
    elif length % 2 == 0:
        dic[(x, y)] = f(int(str(x)[:length//2]), y - 1) + f(int(str(x)[length//2:]), y - 1)
    else:
        dic[(x, y)] = f(x * 2024, y - 1)
    return dic[(x, y)]

print(f"Part 1: {sum([f(val, 25) for val in arr])}")
print(f"Part 2: {sum([f(val, 75) for val in arr])}")


        


