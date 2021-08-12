import sys
import itertools

def main():
    n, s = map(int, sys.stdin.readline().split())
    matrix = list(map(int, sys.stdin.readline().split()))

    num = []
    answer = 0

    for i in range(1, n+1):
        num = list(itertools.combinations(matrix, i))     
        for arr in num:
            if sum(arr) == s:
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()