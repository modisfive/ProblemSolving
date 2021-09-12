from collections import deque
import sys
input = sys.stdin.readline


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    def check():
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 2:
                    bfs((i, j))

        visited = [[0]*m for _ in range(n)]

        def bfs(p):
            que = deque()
            que.append(p)
            while que:
                y, x = que.popleft()
                visited[y][x] = -1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == 2 and visited[ny][nx] == 0:
                        que.append((ny, nx))


main()
