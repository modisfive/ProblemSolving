import sys

input = sys.stdin.readline


n, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(v):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
visited = [0] * (n + 1)


def dfs(node):
    visited[node] = 1
    for i in range(len(matrix[node])):
        if matrix[node][i] == 1 and visited[i] == 0:
            dfs(i)


answer = 0

for i in range(1, n + 1):
    if visited[i] == 0:
        answer += 1
        dfs(i)

print(answer)
