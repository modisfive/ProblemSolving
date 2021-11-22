import sys
from collections import deque

input = sys.stdin.readline


def pArr(arr):
    for i in arr:
        print(i)


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    answer = []

    pArr(matrix)


if __name__ == "__main__":
    main()
