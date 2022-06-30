import sys

input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def go(prev, block):
    path = 0
    if block == "|" or block == "-" or block == "+":
        path = (prev + 2) % 4
    elif block == "1":
        path = 1 - prev
    elif block == "2":
        path = 3 - prev
    elif block == "3":
        path = 5 - prev
    elif block == "4":
        path = 3 - prev

    return path


r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]

y, x = 0, 0
end = (0, 0)

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "M":
            y, x = i, j
        elif matrix[i][j] == "Z":
            end = (i, j)

prev = 0

for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < r and 0 <= nx < c:
        if matrix[ny][nx] != ".":
            y, x = ny, nx
            prev = i
            break
