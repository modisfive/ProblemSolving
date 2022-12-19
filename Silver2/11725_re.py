import sys

sys.setrecursionlimit(10**5)


def main():
    n = int(sys.stdin.readline())
    matrix = [[] * (n + 1) for _ in range(n + 1)]
    for _ in range(n - 1):
        b, a = map(int, sys.stdin.readline().split())
        matrix[b].append(a)
        matrix[a].append(b)

    answer = {}
    check = [False for _ in range(n + 1)]

    def dfs(num):
        for i in matrix[num]:
            if not check[i]:
                answer[i] = num
                check[i] = True
                dfs(i)

    dfs(1)
    for i in range(2, n + 1):
        print(answer[i])


if __name__ == "__main__":
    main()
