import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    dp = [[0]*n for _ in range(n)]

    def dfs(curr):
        y, x = curr
        if dp[y][x]: return dp[y][x]
        dp[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and matrix[y][x] < matrix[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs((ny, nx))+1)
        return dp[y][x]

    for i in range(n):
        for j in range(n):            
            answer = max(answer, dfs((i, j)))
        
    print(answer)

if __name__ == "__main__":
    main()