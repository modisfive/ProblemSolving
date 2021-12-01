import sys

input = sys.stdin.readline


def flip(curr):
    if curr == "H":
        return "T"
    else:
        return "H"


def main():
    n = int(input())
    matrix = [list(input().strip()) for _ in range(n)]

    answer = 9999

    for state in range(1 << n):
        total = 0
        for j in range(n):
            cnt = 0
            for i in range(n):
                curr = matrix[i][j]
                if (state & (1 << i)) != 0:
                    curr = flip(curr)
                if curr == "T":
                    cnt += 1
            total += min(cnt, n - cnt)
        answer = min(answer, total)

    print(answer)


main()
