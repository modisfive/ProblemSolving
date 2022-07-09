import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

max_num = sum(numbers)

flag = [0] * (max_num + 1)

for i in range(1, n + 1):
    combs = list(combinations(numbers, i))
    for comb in combs:
        flag[sum(comb)] = 1

for num in range(1, max_num + 1):
    if flag[num] == 0:
        print(num)
        sys.exit()


print(max_num + 1)
