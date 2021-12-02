import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    gems = [list(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    print(gems)
    print(bags)


main()
