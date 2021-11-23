import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

matrix = list()
virus = list()
visited = list()


def func(n, m, blank_cnt):
    global visited

    visited = copy.deepcopy(matrix)
    que = deque()
    for p in virus:
        que.append(p)
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
                que.append((ny, nx))
                visited[ny][nx] = 2
                blank_cnt -= 1
    return blank_cnt


def main():
    global matrix, virus

    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # blanks = []
    blank_cnt = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                virus.append((i, j))
            elif matrix[i][j] == 0:
                blank_cnt += 1
    # blank_cnt = len(blanks)
    answer = -1

    for y1 in range(n):
        for x1 in range(m):
            if matrix[y1][x1] != 0:
                continue
            for y2 in range(n):
                for x2 in range(m):
                    if matrix[y2][x2] != 0:
                        continue
                    for y3 in range(n):
                        for x3 in range(m):
                            if matrix[y3][x3] != 0:
                                continue
                            if (
                                (y1, x1) == (y2, x2)
                                or (y2, x2) == (y3, x3)
                                or (y3, x3) == (y1, x1)
                            ):
                                continue
                            matrix[y1][x1] = 1
                            matrix[y2][x2] = 1
                            matrix[y3][x3] = 1

                            result = func(n, m, blank_cnt - 3)
                            if answer < result:
                                answer = result

                            matrix[y1][x1] = 0
                            matrix[y2][x2] = 0
                            matrix[y3][x3] = 0
    print(answer)


main()

# for point in blank:
#     matrix[point[0]][point[1]] = 1

# result = func(n, m, blank_cnt - 3)
# if answer < result:
#     answer = result

# for point in blank:
#     matrix[point[0]][point[1]] = 0
