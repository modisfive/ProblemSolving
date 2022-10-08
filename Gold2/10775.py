import sys

input = sys.stdin.readline


g = int(input())
p = int(input())

gates = [0] * (g + 1)

for _ in range(p):
    max_g = int(input())
    flag = True
    for i in range(max_g, 0, -1):
        if gates[i] == 0:
            gates[i] = 1
            flag = False
            break

    if flag:
        break

print(sum(gates))
