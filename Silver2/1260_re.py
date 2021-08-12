import sys
from collections import deque

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    matrix = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = matrix[b][a] = 1
    
    def dfs(start, visited):
        visited += [start]
        for i in range(len(matrix[start])):
            if matrix[start][i] == 1 and (i not in visited):
                dfs(i, visited)
        return visited

    def bfs(start):
        visited = [start]
        que = deque([start])
        while que:
            start = que.popleft()
            for i in range(len(matrix[start])):
                if matrix[start][i] == 1 and (i not in visited):
                    que.append(i)
                    visited.append(i)
        return visited
    
    print(*dfs(s, []))
    print(*bfs(s))

main()