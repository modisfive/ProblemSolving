import sys

input = sys.stdin.readline


n, t = map(int, input().split())
leaks = sorted(list(map(int, input().split())))

start = leaks[0]
cnt = 1

for i in range(1, n):
    if start + t <= leaks[i]:
        start = leaks[i]
        cnt += 1

print(cnt)
