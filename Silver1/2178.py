import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n, m = map(int, sys.stdin.readline().split())                       # 목적지는 matrix[n-1][m-1]
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, list(sys.stdin.readline()[:-1]))))
    
    que = deque()
    x = 0
    y = 0
    # answer = 0                                                          # 언제 answer += 1 이 될 것인가 
    dist = [[0]*m for _ in range(n)]                                                                  
    answer = []
    que.append((y, x))
    dist[y][x] = 1                                                        # 해결책
    while que:
        b, a = que.popleft()
        if matrix[b][a] == 1:
            matrix[b][a] = 0
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<m and 0<=ny<n: 
                    que.append((ny, nx))
                    dist[ny][nx] = dist[b][a] + 1
                    if nx == m-1 and ny == n-1: answer.append(dist[ny][nx])
    print(min(answer))


if __name__ == "__main__":
    main()
