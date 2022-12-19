import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
matrix = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    matrix[a][b] = True
    matrix[b][a] = True

answer = [0] * (n + 1)

que = deque()
que.append(1)
while que:
    parent = que.popleft()
    for child in range(n + 1):
        if matrix[parent][child]:
            answer[child] = parent
            matrix[parent][child] = False
            matrix[child][parent] = False
            que.append(child)

for i in range(2, n + 1):
    print(answer[i])
