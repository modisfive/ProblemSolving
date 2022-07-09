import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0

for i in range(1, n + 1):
    combs = list(combinations(numbers, i))

    for comb in combs:
        if sum(comb) == s:
            answer += 1

print(answer)
