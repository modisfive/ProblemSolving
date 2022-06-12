import sys
from collections import deque

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def go(r, c, matrix):
    visited = [[0] * c for _ in range(r)]

    for x in range(c):
        if matrix[r - 1][x] == "x" and visited[r - 1][x] == 0:
            visited[r - 1][x] = 1
            que = deque()
            que.append((r - 1, x))
            while que:
                y, x = que.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (
                        0 <= nx < c
                        and 0 <= ny < r
                        and visited[ny][nx] == 0
                        and matrix[ny][nx] == "x"
                    ):
                        visited[ny][nx] = 1
                        que.append((ny, nx))

    column = [0] * c
    points = []

    for y in range(r - 1):
        for x in range(c):
            if matrix[y][x] == "x" and visited[y][x] == 0:
                points.append((y, x))
                column[x] = y
                visited[y][x] = 2
                que = deque()
                que.append((y, x))
                while que:
                    y, x = que.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if (
                            0 <= nx < c
                            and 0 <= ny < r
                            and visited[ny][nx] == 0
                            and matrix[ny][nx] == "x"
                        ):
                            visited[ny][nx] = 2
                            column[nx] = max(column[nx], ny)
                            points.append((ny, nx))
                            que.append((ny, nx))
                break

    max_y = max(column)
    diff = 0
    flag = False

    for i in range(1, r - max_y):
        for x, y in enumerate(column):
            if visited[y + i][x] == 1 or y + i == r - 1:
                diff = i
                flag = True
                break
        if flag:
            break

    for p in points:
        y, x = p
        matrix[y][x] = "."

    for p in points:
        y, x = p
        matrix[y + diff][x] = "x"


def main():
    r, c = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(r)]
    n = int(input())
    orders = list(map(lambda x: r - int(x), input().split()))

    for idx, y in enumerate(orders):
        if idx % 2 == 0:
            for x in range(c):
                if matrix[y][x] == "x":
                    matrix[y][x] = "."
                    go(r, c, matrix)
                    break
        else:
            for x in range(c - 1, -1, -1):
                if matrix[y][x] == "x":
                    matrix[y][x] = "."
                    go(r, c, matrix)
                    break

    for row in matrix:
        print("".join(row))


main()
