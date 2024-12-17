import sys

registers = [0, 0, 0]
instructions = []

for line in sys.stdin:
    if line.strip() == "": continue
    l, r = line.strip().split(": ")
    if l == "Register A":
        registers[0] = int(r.strip())
    elif l == "Register B":
        registers[1] = int(r.strip())
    elif l == "Register C":
        registers[2] = int(r.strip())
    elif l == "Program":
        instructions = [*map(int, r.split(","))]

def get_combo(val):
    if val <= 3:
        return val
    else:
        return registers[val - 4]

res = []
idx = 0
while idx < len(instructions):
    a, b, c = registers
    if instructions[idx] == 0:
        a >>= get_combo(instructions[idx + 1])
    elif instructions[idx] == 1:
        b ^= instructions[idx + 1]
    elif instructions[idx] == 2:
        b = get_combo(instructions[idx + 1]) % 8
    elif instructions[idx] == 3:
        if a != 0:
            idx = instructions[idx + 1]
            continue
    elif instructions[idx] == 4:
        b ^= c
    elif instructions[idx] == 5:
        res.append(get_combo(instructions[idx + 1]) % 8)
    elif instructions[idx] == 6:
        b = a >> get_combo(instructions[idx + 1])
    elif instructions[idx] == 7:
        c = a >> get_combo(instructions[idx + 1])
    idx += 2
    registers = [a, b, c]

INF = 1000000000000000000

def dfs(idx, A):
    if idx == -1:
        return A
    A = (A << 3)
    ans = INF
    for i in range(8):
        tmp = A + i
        if (tmp % 8) ^ 5 ^ (tmp >> ((tmp % 8) ^ 1)) % 8 == instructions[idx]:
            ans = min(ans, dfs(idx - 1, tmp))
    return ans


print(f"Part 1: {','.join([*map(str, res)])}")
print(f"Part 2: {dfs(len(instructions) - 1, 0)}")

