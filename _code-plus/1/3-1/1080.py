import sys

input = sys.stdin.readline


def change(y, x):
    global a

    for i in range(y, y + 3):
        for j in range(x, x + 3):
            a[i][j] = 1 - a[i][j]


n, m = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

answer = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            change(i, j)
            answer += 1

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print("-1")
            sys.exit()

print(answer)
