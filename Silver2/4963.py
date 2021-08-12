import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def main():
    answer = []
    
    def bfs(s):
        que = deque()
        que.append(s)
        while que:
            y, x = que.popleft()
            matrix[y][x] = -1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and matrix[ny][nx] == 1:
                    que.append((ny, nx))

    while True:
        m, n = map(int, input().split())
    
        if m == 0 and n == 0: break

        matrix = [list(map(int, input().split())) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m): 
                if matrix[i][j] == 1:
                    bfs((i, j))
                    res += 1
        answer.append(res)

    for i in answer: print(i)

if __name__ == "__main__":
    main()