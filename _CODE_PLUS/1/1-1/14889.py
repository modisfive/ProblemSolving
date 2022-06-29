import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

combs = list(combinations(range(n), n // 2))

answer = float("inf")

for comb in combs:
    team1 = 0
    for i in comb:
        for j in comb:
            team1 += matrix[i][j]
    team2 = 0
    for i in range(n):
        if i not in comb:
            for j in range(n):
                if j not in comb:
                    team2 += matrix[i][j]

    answer = min(answer, abs(team1 - team2))

print(answer)
