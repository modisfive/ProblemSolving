import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

hx = [2, 1, -1, -2, -2, -1, 1, 2]
hy = [-1, -2, -2, -1, 1, 2, 2, 1]

def main():
    cnt = int(input())
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0]*m for _ in range(n)]

    def bfs():
        nonlocal cnt
        que = deque()
        que.append((0, 0, cnt))
        visited[0][0] = 1
        while que:
            y, x, cnt = que.popleft()
            if cnt:
                for i in range(8):
                    nx = x + hx[i]
                    ny = y + hy[i]
                    if 0<=nx<m and 0<=ny<n and matrix[ny][nx] == 0 and (visited[ny][nx] == 0 or visited[y][x]+1<visited[ny][nx]):
                        visited[ny][nx] = visited[y][x] + 1
                        que.append((ny, nx, cnt-1))
                        if (ny, nx) == (n-1, m-1): return visited[ny][nx]-1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and matrix[ny][nx] == 0 and (visited[ny][nx] == 0 or visited[y][x]+1<visited[ny][nx]):
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx, cnt))
                    if (ny, nx) == (n-1, m-1): return visited[ny][nx]-1
        
        return -1

    print(bfs())

if __name__ == "__main__":
    main()