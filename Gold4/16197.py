import sys
from collections import deque

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)


def main():
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    coins = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "o":
                coins.extend([i, j])

    trace_1 = [[0] * m for _ in range(n)]
    trace_2 = [[0] * m for _ in range(n)]

    def bfs(start):
        que = deque()
        que.append(start)
        while que:
            y_1, x_1, y_2, x_2, count = que.popleft()
            trace_1[y_1][x_1] = 1
            trace_2[y_2][x_2] = 1
            count += 1
            if count > 10:
                return -1
            for i in range(4):
                ny_1 = y_1 + dy[i]
                nx_1 = x_1 + dx[i]
                ny_2 = y_2 + dy[i]
                nx_2 = x_2 + dx[i]

                if (
                    (0 <= ny_1 < n and 0 <= nx_1 < m)
                    and not (0 <= ny_2 < n and 0 <= nx_2 < m)
                ) or (
                    not (0 <= ny_1 < n and 0 <= nx_1 < m)
                    and (0 <= ny_2 < n and 0 <= nx_2 < m)
                ):
                    return count

                elif (
                    (0 <= ny_1 < n and 0 <= nx_1 < m)
                    and (0 <= ny_2 < n and 0 <= nx_2 < m)
                    and (trace_1[ny_1][nx_1] == 0 and trace_2[ny_2][nx_2] == 0)
                    and not (matrix[ny_1][nx_1] == "#" and matrix[ny_2][nx_2] == "#")
                ):
                    if matrix[ny_1][nx_1] == "#":
                        ny_1 = y_1
                        nx_1 = x_1
                    if matrix[ny_2][nx_2] == "#":
                        ny_2 = y_2
                        nx_2 = x_2
                    que.append([ny_1, nx_1, ny_2, nx_2, count])

    answer = bfs(coins + [0])
    if answer is None:
        answer = -1
    print(answer)


main()
