import sys
from collections import deque

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def pArr(arr):
    for i in arr:
        print(i)


def find(n, matrix, visited):
    results = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if 0 < matrix[i][j] and visited[i][j] == 0:
                cnt += 1
                rainbow = 0
                size = 1
                tmp = [(i, j)]
                color = matrix[i][j]
                visited[i][j] = cnt
                que = deque()
                que.append((i, j))
                while que:
                    y, x = que.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if (
                            0 <= nx < n
                            and 0 <= ny < n
                            and visited[ny][nx] != cnt
                            and (matrix[ny][nx] == 0 or matrix[ny][nx] == color)
                        ):
                            if matrix[ny][nx] == 0:
                                rainbow += 1
                            elif matrix[ny][nx] == color:
                                tmp.append((ny, nx))
                            visited[ny][nx] = cnt
                            size += 1
                            que.append((ny, nx))
                if size >= 2:
                    py, px = sorted(tmp, key=lambda x: (x[0], x[1]))[0]
                    results.append((size, rainbow, py, px, cnt))
    return results


def delete(n, matrix, visited, py, px, cnt):
    que = deque()
    que.append((py, px))
    color = matrix[py][px]
    matrix[py][px] = False
    visited[py][px] = -1
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (
                0 <= ny < n
                and 0 <= nx < n
                and (
                    (matrix[ny][nx] == 0 and visited[ny][nx] != -1)
                    or (matrix[ny][nx] == color and visited[ny][nx] == cnt)
                )
            ):
                matrix[ny][nx] = False
                visited[ny][nx] = -1
                que.append((ny, nx))


def apply_gravity(n, matrix):
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if matrix[i][j] is not False and matrix[i][j] != -1:
                y = i
                while y + 1 < n and matrix[y + 1][j] is False:
                    matrix[y + 1][j] = matrix[y][j]
                    matrix[y][j] = False
                    y += 1


def rotate(matrix):
    matrix = [list(arr) for arr in zip(*matrix)][::-1]


def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    answer = 0

    while True:
        visited = [[0] * n for _ in range(n)]

        results = find(n, matrix, visited)

        if len(results) == 0:
            break

        size, _, py, px, cnt = sorted(
            results, key=lambda x: (-x[0], -x[1], -x[2], -x[3])
        )[0]

        answer += size**2

        delete(n, matrix, visited, py, px, cnt)

        apply_gravity(n, matrix)
        rotate(matrix)
        apply_gravity(n, matrix)

    print(answer)


main()
