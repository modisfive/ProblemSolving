import sys
import copy
sys.setrecursionlimit(10**5)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    m, n = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    start_x, start_y = 0, 0
    melted = 0
    
    # 한 덩이의 count 시작할 위치
    stop = False
    for i in range(1, m-1):
        for j in range(1, n-1):
            if matrix[i][j] != 0:
                start_x, start_y = j, i
                stop = True
                break
        if stop == True: break

    def getCnt():               # 한 덩이의 빙산의 갯수를 세자
        nonlocal start_x, start_y, matrix
        visited = [[0]*n for _ in range(m)]
        cnt = 0
        stop = False

        def dfs(y, x):
            nonlocal cnt
            visited[y][x] = 1
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if matrix[ny][nx] != 0 and visited[ny][nx] == 0:
                    dfs(ny, nx)

        if matrix[start_y][start_x] == 0:
            for i in range(start_y, m-1):
                for j in range(start_x, n-1):
                    if matrix[i][j] != 0:
                        start_x, start_y = j, i
                        stop = True
                        break
                if stop == True: break

        dfs(start_y, start_x)
                        
        return cnt

    def shrink():
        nonlocal matrix, melted
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
                        cnt += 1
                        
        matrix = tmp
        melted += cnt
              
    answer = 0
    start = getCnt()
   
    while True:
        answer += 1
        shrink()
        if melted == start:
            print(0)
            break
        elif getCnt() + melted != start:
            print(answer)
            break

if __name__ == "__main__":
    main()