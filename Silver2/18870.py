import sys
from collections import defaultdict

input = sys.stdin.readline


n = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(list(set(numbers)))
curr = sorted_numbers[0]
convert = defaultdict(int)
for i in range(1, len(sorted_numbers)):
    if sorted_numbers[i] != curr:
        convert[sorted_numbers[i]] = convert[curr] + 1
        curr = sorted_numbers[i]

answer = []
for n in numbers:
    answer.append(convert[n])

print(*answer)
