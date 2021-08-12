import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(n)]

    def bfs(start):
        que = deque()
        que.append(start)
        while que:
            y, x = que.popleft()
            matrix[y][x] = -1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and matrix[ny][nx] == 0:
                    que.append((ny, nx))
    
    for i in range(m):
        if matrix[0][i] == 0: bfs((0, i))

    answer = "NO"
    for i in range(m):
        if matrix[n-1][i] == -1: 
            answer = "YES"
            break

    print(answer)


if __name__ == "__main__":
    main()