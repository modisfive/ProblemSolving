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

    matrix = [list(input().strip()) for _ in range(n)]

    start = 0
    f = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'J': 
                matrix[i][j] = 1
                start = (i, j)
            if matrix[i][j] == 'F': f.append((i, j))

    def bfs():
        que = deque()
        que.append(start)
        while que:
            y, x = que.popleft()
            if matrix[y][x] == 'F': continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and matrix[ny][nx] == '.':
                    matrix[ny][nx] = matrix[y][x] + 1
                    que.append((ny, nx))
                    if ny in (0, n-1) or nx in (0, m-1): return matrix[ny][nx]
            fire()
        return "IMPOSSIBLE"
        
    def fire(): 
        que = deque(f)   
        for _ in range(len(que)):
            y, x = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and matrix[ny][nx] != '#':
                    matrix[ny][nx] = 'F'
                    f.append((ny, nx))
 
    pArr(matrix)
    print(bfs())

if __name__ == "__main__":
    main()