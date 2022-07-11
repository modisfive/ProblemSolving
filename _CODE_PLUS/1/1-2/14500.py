import sys
from itertools import permutations

input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

tets = [
    [(0, 1), (1, 1), (0, 2)],
    [(-1, 1), (0, 1), (1, 1)],
    [(1, 0), (1, -1), (1, 1)],
    [(1, 0), (1, 1), (2, 0)],
]

tets += list(permutations(d, 3))


def get_score(y, x, tet):
    result = 0
    for dy, dx in tet:
        ny = y + dy
        nx = x + dx
        if not (0 <= ny < n and 0 <= nx < m):
            return -1
        result += matrix[ny][nx]
    return result


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

answer = -1

for tet in tets:
    for y in range(n):
        for x in range(m):
            score = get_score(y, x, tet)
            answer = max(answer, score)

print(answer)
