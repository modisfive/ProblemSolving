import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[b].append(a)

results = []
max_cnt = -float("INF")


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    que = deque()
    que.append(i)
    visited[i] = True
    cnt = 1
    while que:
        curr = que.popleft()
        for nxt in matrix[curr]:
            if not visited[nxt]:
                cnt += 1
                visited[nxt] = True
                que.append(nxt)

    if max_cnt < cnt:
        results = [i]
        max_cnt = cnt
    elif cnt == max_cnt:
        results.append(i)

print(*results)
