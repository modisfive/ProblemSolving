import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
tmp = list(map(int, input().split()))

ops = []

for i, v in enumerate(tmp):
    for _ in range(v):
        ops.append(i)

answers = []

for order in set(permutations(ops, n - 1)):
    result = numbers[0]
    for idx in range(n - 1):
        if order[idx] == 0:
            result += numbers[idx + 1]
        elif order[idx] == 1:
            result -= numbers[idx + 1]
        elif order[idx] == 2:
            result *= numbers[idx + 1]
        elif order[idx] == 3:
            result /= numbers[idx + 1]
            result = int(result)
    answers.append(result)

print(max(answers))
print(min(answers))
