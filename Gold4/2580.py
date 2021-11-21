import sys

input = sys.stdin.readline


def main():
    matrix = [list(map(int, input().split())) for _ in range(9)]

    for i in matrix:
        print(i)


main()
