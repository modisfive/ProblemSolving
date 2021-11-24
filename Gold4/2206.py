import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def pArr(arr):
    for i in arr:
        print(i)


def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[9999] * m for _ in range(n)]

    def bfs():
        que = deque()
        que.append((0, 0, 1))
        visited[0][0] = 1
        while que:
            y, x, cnt = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and visited[y][x] + 1 < visited[ny][nx]
                    and matrix[ny][nx] == 0
                ):
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx, cnt))
                if (
                    cnt == 1
                    and 0 <= nx < m
                    and 0 <= ny < n
                    and visited[y][x] + 1 < visited[ny][nx]
                    and matrix[ny][nx] == 1
                ):
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx, 0))

    bfs()

    answer = visited[n - 1][m - 1] if visited[n - 1][m - 1] != 9999 else -1
    print(answer)
    pArr(visited)


main()
