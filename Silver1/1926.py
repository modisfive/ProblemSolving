import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    visited = [[0]*n for _ in range(m)]

    def bfs(p):
        y, x = p
        matrix[y][x] = -1

        que = deque()
        que.append(p)
        cnt = 0

        while que:
            y, x = que.popleft()
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and matrix[ny][nx] == 1:
                    matrix[ny][nx] = -1
                    que.append((ny, nx))

        return cnt

    answer = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                answer.append(bfs((i,j)))

    print(len(answer))
    print(max(answer)) if len(answer) != 0 else print(0)

if __name__ == "__main__":
    main()