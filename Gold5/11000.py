import sys

input = sys.stdin.readline


n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort(key=lambda x: (x[0], x[1] - x[0]))

time = 0
answer = 0

for start, end in classes:
    if time <= start:
        answer += 1


print(answer)
