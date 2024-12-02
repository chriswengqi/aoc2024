import sys

ans = 0

def check_valid(lst):
    inc = lst[1] > lst[0]
    valid = True
    for i in range(1, len(lst)):
        if (inc and (lst[i] <= lst[i - 1] or lst[i] > lst[i - 1] + 3)) or (not inc and (lst[i] >= lst[i - 1] or lst[i] < lst[i - 1] - 3)):
            valid = False
            break
    return valid

for line in sys.stdin:
    lst = [*map(int, line.strip().split())]
    ans += check_valid(lst)

print(ans)
        