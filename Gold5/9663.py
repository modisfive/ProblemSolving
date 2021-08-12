import sys

def main():
    n = int(sys.stdin.readline())
    col = [0]*n

    def isFit(x):
        for i in range(x):
            if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
                return False
        return True

    answer = 0

    def dfs(s):
        nonlocal answer
        if s == n: answer += 1 
        else:
            for i in range(n):
                col[s] = i
                if isFit(s):
                    dfs(s+1)

    dfs(0)
    print(answer)


if __name__ == "__main__":
    main()