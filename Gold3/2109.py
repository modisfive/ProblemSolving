import sys

input = sys.stdin.readline


def pArr(arr):
    for i in arr:
        print(i)


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    matrix.sort(key=lambda x: x[1])

    length = matrix[-1][1]

    print(length)

    for day in range(length):
        temp = []
        for arr in range(matrix):
            if day <= arr[1]:
                temp.append(arr)

        temp.sort(key=lambda x: x[0])


main()
