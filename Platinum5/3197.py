import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def main():
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    start = []
    icebergs = []
    num = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "L":
                matrix[i][j] = num
                start.append((i, j))
                num += 1
            elif matrix[i][j] == "X":
                matrix[i][j] = -1
                icebergs.append((i, j))
            else:
                matrix[i][j] = 0

    def go(y, x, day):
        que = deque()
        que.append((y, x))
        while que:
            y, x = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and matrix[ny][nx] != -1
                    and matrix[ny][nx] != matrix[y][x]
                ):
                    if matrix[ny][nx] == 3 - matrix[y][x]:
                        print(day)
                        sys.exit(0)
                    else:
                        matrix[ny][nx] = matrix[y][x]
                        que.append((ny, nx))

    def melt(matrix, icebergs):
        tmp = []
        next_start = []
        melted = []
        unmelted = []
        for y, x in icebergs:
            flag = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] != -1:
                    if matrix[ny][nx] != 0:
                        tmp.append((y, x, matrix[ny][nx]))
                        next_start.append((y, x))
                    else:
                        melted.append((y, x))
                    flag = False
                    break
            if flag:
                unmelted.append((y, x))

        icebergs = unmelted

        for y, x in melted:
            matrix[y][x] = 0

        for y, x, num in tmp:
            matrix[y][x] = num

        return next_start

    day = 0

    while True:
        for y, x in start:
            go(y, x, day)
        start = melt(matrix, icebergs)
        day += 1


main()
