import sys
from collections import deque

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)


def pArr(arr):
    for i in arr:
        print(i)


def func(prev, curr):
    if (prev == (0, 1) or prev == (0, -1)) and (curr == (1, 0) or curr == (-1, 0)):
        return True
    elif (prev == (1, 0) or prev == (-1, 0)) and (curr == (0, 1) or curr == (0, -1)):
        return True
    else:
        return False


def main():
    w, h = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(h)]

    start = 0
    dest = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "C":
                if not start:
                    start = [i, j]
                else:
                    dest = [i, j]

    def bfs(start):
        que = deque()
        que.append(start)
        visited = [[0] * w for _ in range(h)]
        while que:
            y, x, prev, cnt = que.popleft()
            visited[y][x] = 1
            if (y, x) == dest:
                return cnt
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < w
                    and 0 <= ny < h
                    and matrix[ny][nx] != "*"
                    and visited[ny][nx] == 0
                ):
                    curr = (dy[i], dx[i])
                    if func(prev, curr):
                        que.append((ny, nx, curr, cnt + 1))
                    else:
                        que.append((ny, nx, curr, cnt))
        pArr(visited)

    print(bfs(start + [(0, 0), 0]))


main()
