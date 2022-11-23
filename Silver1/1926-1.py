# 메모리 초과

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
paints = 0
max_size = 0


def dfs(y, x):
    cnt = 1
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1 and not visited[ny][nx]:
            cnt += dfs(ny, nx)
    return cnt


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            paints += 1
            max_size = max(max_size, dfs(i, j))


print(paints)
print(max_size)
