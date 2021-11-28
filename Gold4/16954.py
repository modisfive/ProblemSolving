import sys
from collections import deque

input = sys.stdin.readline

dx = (1, 1, 0, -1, -1, -1, 0, 1, 0)
dy = (0, -1, -1, -1, 0, 1, 1, 1, 0)


def pArr(arr):
    for i in arr:
        print(i)


def main():
    matrix = [list(input().strip()) for _ in range(8)]

    def wall_move():
        nonlocal matrix

        matrix = [["."] * 8] + matrix
        del matrix[-1]

    def bfs(start):
        visited = [[-1] * 8 for _ in range(8)]
        visited[7][7] = 0
        que = deque()
        que.append(start)
        while que:
            pArr(matrix)
            print()
            y, x = que.popleft()
            if matrix[y][x] == "#":
                continue
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < 8
                    and 0 <= ny < 8
                    and visited[ny][nx] == -1
                    and matrix[ny][nx] == "."
                ):
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx))
            wall_move()
        return visited[0][7]

    print(bfs((7, 7)))


main()
