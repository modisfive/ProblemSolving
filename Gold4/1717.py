import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    maps = [-1] * (n + 1)

    group = 0

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            if maps[a] == -1 and maps[b] == -1:
                maps[a] = group
                maps[b] = group
            elif maps[b] == -1:
                maps[b] = maps[a]
            


main()
