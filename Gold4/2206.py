import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def pArr(arr):
    for i in arr:
        print(i)

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    def bfs():
        que = deque()
        que.append((0, 0, 1))
        visited[0][0] = 1
        while que:
            y, x, cnt = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0 and matrix[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx, cnt))
                if cnt == 1 and 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0 and matrix[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx, 0))
            
        
    bfs()

    # if visited[n-1][m-1] == 0: print(-1)
    # else: print(visited[n-1][m-1])

    pArr(visited)

if __name__ == "__main__":
    main()