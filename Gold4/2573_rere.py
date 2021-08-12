import sys
import copy
sys.setrecursionlimit(10**5)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    m, n = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    def getCnt():
        nonlocal matrix
        visited = [[0]*n for _ in range(m)]
        cnt = 0

        def dfs(y, x):
            visited[y][x] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if matrix[ny][nx] != 0 and visited[ny][nx] == 0:
                    dfs(ny, nx)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if matrix[i][j] != 0 and visited[i][j] == 0:
                    dfs(i, j)
                    cnt += 1
                        
        return cnt

    def shrink():
        nonlocal matrix
        cnt = 0   
        tmp = copy.deepcopy(matrix)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if matrix[i][j] != 0:
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if matrix[ny][nx] == 0:
                            tmp[i][j] -= 1 
                        if tmp[i][j] <= 0:
                            tmp[i][j] = 0
                        
        matrix = tmp

                            
    answer = 0
    while True:
        answer += 1
        shrink()
        if getCnt() > 1:
            print(answer)
            break
    

if __name__ == "__main__":
    main()