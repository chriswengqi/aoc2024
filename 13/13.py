import sys
from math import gcd

arr1, arr2, res = [], [], []
CONST = 10000000000000

for line in sys.stdin:
    if line.strip() == "": continue
    title, l = line.strip().split(": ")
    x, y = l.strip().split(", ")
    if title == "Button A":
        _, a = x.strip().split("+")
        _, b = y.strip().split("+")
        arr1.append((int(a), int(b)))
    elif title == "Button B":
        _, a = x.strip().split("+")
        _, b = y.strip().split("+")
        arr2.append((int(a), int(b)))
    else:
        _, a = x.strip().split("=")
        _, b = y.strip().split("=")
        res.append((int(a), int(b)))

ans1, ans2 = 0, 0

# Solves a1 * a + b1 * b = c1; a2 * a + b2 * b = c2;
# Returns None, None if no solution

def simultaneous_equation(a1, a2, b1, b2, c1, c2):
    lcm = a1 * a2 // gcd(a1, a2)
    b1 *= lcm // a1
    b2 *= lcm // a2
    c1 *= lcm // a1
    c2 *= lcm // a2

    if b2 - b1 == 0 or (c2 - c1) % (b2 - b1) != 0:
        return None, None
    b = (c2 - c1) // (b2 - b1)

    if (c1 - b1 * b) % a1 != 0:
        return None, None
    a = (c1 - b1 * b) // lcm 

    return a, b

for i in range(len(arr1)):
    a1, a2 = arr1[i]
    b1, b2 = arr2[i]
    c1, c2 = res[i]

    a, b = simultaneous_equation(a1, a2, b1, b2, c1, c2)
    if a and b and 0 <= a <= 100  and 0 <= b <= 100:
        ans1 += 3*a  + b
    a, b = simultaneous_equation(a1, a2, b1, b2, c1 + CONST, c2 + CONST)
    if a and b and a >= 0 and b >= 0:
        ans2 += 3*a + b


print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")
    




