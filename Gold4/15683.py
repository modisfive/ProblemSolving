import sys
from copy import deepcopy

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]


def pArr(arr):
    for i in arr:
        print(i)


def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    cctv = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] in (1, 2, 3, 4, 5):
                cctv.append((i, j))

    def go(arr, y, x, d):
        for i in d:
            ny = y + dy[i]
            nx = x + dx[i]
            while 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 6:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = "#"
                ny += dy[i]
                nx += dx[i]

    answer = 9999

    def solve(idx, maps):
        nonlocal answer
        if idx == len(cctv):
            tmp = 0
            for arr in maps:
                tmp += arr.count(0)
            answer = min(answer, tmp)
            return

        y, x = cctv[idx]
        arr = deepcopy(maps)

        for d in direction[maps[y][x]]:
            go(arr, y, x, d)
            solve(idx + 1, arr)
            arr = deepcopy(maps)

    solve(0, matrix)

    print(answer)


main()
