import sys
from collections import deque

answer = 0
baby = 2

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

def main():
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    b, a = 0, 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 9:
                b, a = i, j

    def bfs(b, a):
        global answer
        global baby

        que = deque()
        que.append((b, a))
        visited = [[0]*n for _ in range(n)]
        while que:
            y, x = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and (matrix[ny][nx] <= baby or matrix[ny][nx] == 0) and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny, nx))
                if 0<=nx<n and 0<=ny<n and 0 < matrix[ny][nx] < baby: 
                    answer += visited[ny][nx]
                    matrix[ny][nx] = 9
                    matrix[b][a] = 0
                    b, a = ny, nx
                    return 
    
    while True:
        edible = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < baby: edible += 1
                else: 
                    print(answer)
                    sys.exit()

        cnt = 0
        for _ in range(edible):
            bfs(b, a)
            cnt += 1
            if cnt == baby: baby += 1





if __name__ == "__main__":
    main()