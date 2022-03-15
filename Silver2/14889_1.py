import sys
from itertools import combinations

input = sys.stdin.readline


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    tmp = list(combinations(range(n), n // 2))

    result = 9999

    for arr in tmp:
        answer1 = 0
        for i in arr:
            for j in arr:
                answer1 += matrix[i][j]
        answer2 = 0
        for i in range(n):
            if i not in arr:
                for j in range(n):
                    if j not in arr:
                        answer2 += matrix[i][j]
        if abs(answer1 - answer2) < result:
            result = abs(answer1 - answer2)

    print(result)


main()
