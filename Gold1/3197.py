import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    location = (0, 0)
    stop = False

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'L': 
                location = (i, j)
                stop = True
                break
        if stop: break

    def bfs():
        que = deque()
        que.append(location)
        visited = [[0]*m for _ in range(n)]
        while que:
            y, x = que.popleft()
            visited[y][x] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and matrix[ny][nx] != 'X' and visited[ny][nx] == 0:
                    que.append((ny, nx))
                    if matrix[ny][nx] == 'L': return True

    def melt():
        tmp = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'X':
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if 0<=nx<m and 0<=ny<n and matrix[ny][nx] != 'X':
                            tmp.append((i, j))
                            break
        for point in tmp:
            matrix[point[0]][point[1]] = '.'

    day = 0
    while True:
        if bfs(): break
        melt()
        day += 1
    print(day)


if __name__ == "__main__":
    main()