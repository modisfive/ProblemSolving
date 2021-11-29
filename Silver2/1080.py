import sys

input = sys.stdin.readline


def pArr(arr):
    for i in arr:
        print(i)


def main():
    n, m = map(int, input().split())
    matrix_from = [list(map(int, input().strip())) for _ in range(n)]
    matrix_to = [list(map(int, input().strip())) for _ in range(n)]
    matrix = [[0] * m for _ in range(n)]

    if n < 3 or m < 3:
        print(-1)
        return

    for i in range(n):
        for j in range(m):
            if matrix_from[i][j] != matrix_to[i][j]:
                matrix[i][j] = 1
    pArr(matrix_from)
    print()
    pArr(matrix_to)
    print()
    pArr(matrix)


main()
