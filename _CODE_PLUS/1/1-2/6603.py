import sys
from itertools import combinations

input = sys.stdin.readline


while True:
    numbers = list(map(int, input().split()))

    if len(numbers) == 1 and numbers[0] == 0:
        break

    k = numbers[0]
    numbers = numbers[1:]

    combs = list(combinations(numbers, 6))

    for comb in combs:
        for i in comb:
            print(i, end=" ")
        print()
    print()
