import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(curr):
    visited[curr] = True

    for _next in graph[curr]:
        if not visited[_next]:
            dfs(_next)

            dp[curr][0] += dp[_next][1]
            dp[curr][1] += min(dp[_next])


n = int(input())

graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

dp = [[0, 1] for _ in range(n + 1)]

dfs(1)

print(min(dp[1]))