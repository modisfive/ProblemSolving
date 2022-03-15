import sys
from itertools import permutations

input = sys.stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    a = list(map(int, input().split()))

    tmp = []

    for idx, value in enumerate(a):
        for _ in range(value):
            tmp.append(idx)

    results = []

    for ordering in set(permutations(tmp)):
        answer = arr[0]
        for b in range(len(ordering)):
            if ordering[b] == 0:
                answer += arr[b + 1]
            elif ordering[b] == 1:
                answer -= arr[b + 1]
            elif ordering[b] == 2:
                answer *= arr[b + 1]
            elif ordering[b] == 3:
                answer /= arr[b + 1]
                answer = int(answer)
        results.append(answer)

    print(max(results))
    print(min(results))


main()
