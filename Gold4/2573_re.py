import sys
import copy
sys.setrecursionlimit(10**5)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    m, n = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    def lumpAndShrink():
        visited = [[0]*n for _ in range(m)]
        answer = 0                              # 덩이의 갯수
        tmparr = copy.deepcopy(matrix)

        def dfs(y, x):
            visited[y][x] = 1
            tmp = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if matrix[ny][nx] != 0 and visited[ny][nx] == 0:
                    dfs(ny, nx)
                if matrix[ny][nx] == 0:
                    tmp += 1
                    
            if tmparr[y][x] < tmp: tmparr[y][x] = 0
            else: tmparr[y][x] -= tmp

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0 and visited[i][j] == 0:
                    answer += 1
                    dfs(i, j)

        return (tmparr, answer)

    cnt = 0
    while True:
        matrix, res = lumpAndShrink()
        cnt += 1
        print(matrix, res)
        if res >= 2: break
    print(cnt)

    
    


if __name__ == "__main__":
    main()