import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    m, n = map(int, sys.stdin.readline().split())
    matrix = [list(map(str, sys.stdin.readline().strip())) for _ in range(m)]

    def bfs(start):
        nonlocal answer
        y, x = start
        que = deque()
        que.append((y, x, matrix[y][x]))
        while que:
            y, x, string = que.popleft()
            answer = max(answer, len(string))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and matrix[ny][nx] not in string:
                    que.append((ny, nx, string + matrix[ny][nx]))
                    
    answer = 1
    bfs((0, 0))
    print(answer)


if __name__ == "__main__":
    main()