import sys

input = sys.stdin.readline


n, m = map(int, input().split())
visited = [False] * (n + 1)


def go(arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            go(arr + [i])
            visited[i] = False


go([])
