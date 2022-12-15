import sys

input = sys.stdin.readline


n, k = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]

target = None

for nation in nations:
    if nation[0] == k:
        target = nation
        break

answer = 1

for nation in nations:
    if nation[0] == k:
        continue

    if nation[1] > target[1]:
        answer += 1

    elif nation[1] == target[1] and nation[2] > target[2]:
        answer += 1

    elif nation[1] == target[1] and nation[2] == target[2] and nation[3] > target[3]:
        answer += 1

print(answer)
