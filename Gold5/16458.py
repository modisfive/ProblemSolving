# 0 12
# 1 8
# 2 8
# 3 10
# 4 9
# 5 10
# 6 10
# 7 7
# 8 13
# 9 10

import sys
input = sys.stdin.readline
from collections import deque

dx = (1, 1, 0, -1, -1, -1, 0, 1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

shapes = [
    [
        "***",
        "* *",
        "* *",
        "* *",
        "***"
    ],
    [
        "** ",
        " * ",
        " * ",
        " * ",
        "***"
    ],
    [
        "** ",
        "  *",
        " * ",
        "*  ",
        "***"
    ],
    [
        "***",
        "  *",
        " **",
        "  *",
        "***"
    ],
    [
        "  *",
        " **",
        "* *",
        "***",
        "  *"
    ],
    [
        "***",
        "*  ",
        "** ",
        "  *",
        "***"
    ],
    [
        "*  ",
        "*  ",
        "***",
        "* *",
        "***"
    ],
    [
        "***",
        "  *",
        " * ",
        "*  ",
        "*  "
    ],
    [
        "***",
        "* *",
        "***",
        "* *",
        "***"
    ],
    [
        "***",
        "* *",
        "***",
        "  *",
        "  *"
    ]
]

def pArr(arr):
    for i in arr:
        print(i)

def main():
    n, m = map(int, input().split())
    matrix = [list(input())[:-1] for _ in range(n)]

    visited = [[0]*m for _ in range(n)]

    def bfs(p):
        y, x = p
        visited[y][x] = -1
        cnt = 1
        que = deque()
        que.append(p)
        while que:
            y, x = que.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0 and matrix[ny][nx] == "*":
                    que.append((ny, nx))
                    visited[ny][nx] = -1
                    cnt += 1

        return cnt

    answer = {}

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "*" and visited[i][j] == 0:
                answer['({}, {})'.format(i, j)] = bfs((i, j))

    print(max(answer))
        

main()