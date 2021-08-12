import sys
answer = 0
def main():
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        matrix[b][a] = 1

    def dfs(start, cnt, m, n):
        global answer
        num1, num2 = start

        if matrix[num1][num2] == 1:
            matrix[num1][num2] = 0
            if cnt == 0: answer += 1

            if num2 != m-1: dfs((num1, num2+1), cnt+1, m, n)
            if num1 != n-1: dfs((num1+1, num2), cnt+1, m, n)
            if num1 != 0: dfs((num1-1, num2), cnt+1, m, n)
            if num2 != 0: dfs((num1, num2-1), cnt+1, m, n)
    for i in range(n):
        for j in range(m):
            dfs((i, j), 0, m, n)
    print(answer)
    
if __name__ == "__main__":
    main()