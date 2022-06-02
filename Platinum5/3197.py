import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def main():
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    swans = []
    icebergs = []
    mark = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "L":
                swans.append((i, j))
            elif matrix[i][j] == "X":
                icebergs.append((i, j))

    def go(y, x, num, day):
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
                    and matrix[ny][nx] != "X"
                    and mark[ny][nx] != num
                ):
                    if mark[ny][nx] == 3 - num:
                        print(day)
                        return
                    else:
                        mark[ny][nx] = num
                        que.append((ny, nx))

    def melt(matrix, mark):
        melted = []
        unmelted = []
        for y, x in icebergs:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == ".":
                    if mark[ny][nx] != 0:
                        


main()
