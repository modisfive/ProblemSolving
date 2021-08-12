import sys
import copy
sys.setrecursionlimit(10**5)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    m, n = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    def lump():
        visited = [[0]*n for _ in range(m)]
        answer = 0

        def dfs(y, x):
            visited[y][x] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if matrix[ny][nx] != 0 and visited[ny][nx] == 0:
                    dfs(ny, nx)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0 and visited[i][j] == 0:
                    answer += 1
                    dfs(i, j)

        return answer

    def shrink():
        tmparr = copy.deepcopy(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    tmp = 0
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if matrix[ny][nx] == 0: tmp += 1
                    if tmparr[i][j] < tmp: tmparr[i][j] = 0
                    else: tmparr[i][j] -= tmp
        return tmparr

    result = 0                        
    while(lump() < 2):
        result += 1
        matrix = shrink()
    print(result)
    
    


if __name__ == "__main__":
    main()