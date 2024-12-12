import sys

s = ""
for line in sys.stdin:
    s = line.strip()
curr = []
ctr = 0
for i, char in enumerate([*s]):
    if i % 2 == 0:
        for j in range(int(char)):
            curr.append(ctr)
        ctr += 1
    else:
        for j in range(int(char)):
            curr.append("")

l = 0
r = len(curr) - 1
ans = 0
while l <= r:
    if curr[l] == "":
        curr[l], curr[r] = curr[r], curr[l]
    ans += l * curr[l]
    l += 1
    while curr[r] == "":
        r -= 1

print(ans)

