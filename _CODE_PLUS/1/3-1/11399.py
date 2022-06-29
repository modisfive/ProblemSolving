import sys

input = sys.stdin.readline

n = int(input())
ts = list(map(int, input().split()))

ts.sort()

answer = 0

for i in range(n):
    answer += sum(ts[: i + 1])

print(answer)
