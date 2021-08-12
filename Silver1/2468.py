import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n = int(sys.stdin.readline())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    def bfs(s, h, visited):
        que = deque()
        que.append(s)
        while que:
            b, a = que.popleft()
            visited[b][a] = 1
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n and matrix[ny][nx] > h and visited[ny][nx] == 0:
                    que.append((ny, nx))        
        return 1

    MAX = 0                    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > MAX: MAX = matrix[i][j]
    result = [0]*MAX
    for h in range(MAX):
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > h and visited[i][j] == 0:
                    result[h] += bfs((i, j), h, visited)
    print(max(result))

if __name__ == "__main__":
    main()