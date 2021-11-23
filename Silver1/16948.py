import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, -2, 2, -1, 1]
dy = [-2, -2, 0, 0, 2, 2]


def func(n, start, dest):
    visited = [[0] * n for _ in range(n)]
    r, c = start
    visited[r][c] = 1

    result = 0

    que = deque()
    que.append(start)
    while que:
        y, x = que.popleft()
        if (y, x) == dest:
            result = visited[y][x]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                que.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    return result - 1 if result else -1


def main():
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    answer = func(n, (r1, c1), (r2, c2))

    print(answer)


main()
