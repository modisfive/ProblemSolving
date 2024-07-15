import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
count = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                count[i][j] = 1

answer = 0
for row in count:
    answer = max(answer, sum(row))


print(answer)