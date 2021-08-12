import sys
from collections import deque
import copy

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def main():
    n = int(sys.stdin.readline())
    li = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
    
    def bfs(arr, s, color):
        que = deque()
        que.append(s)
        while que:
            b, a = que.popleft()
            arr[b][a] = 0
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n and arr[ny][nx] == color:
                    que.append((ny, nx))

    for i in range(n):
        for j in range(n):
            if li[i][j] == 'R':
                li[i][j] = 1
            elif li[i][j] == 'G':
                li[i][j] = 2
            else: li[i][j] = 3

    rg = copy.deepcopy(li)

    for i in range(n):
        for j in range(n):
            if rg[i][j] == 2:
                rg[i][j] = 1

    answer1 = 0
    answer2 = 0

    for i in range(n):
        for j in range(n):
            if li[i][j] != 0:
                answer1 += 1
                bfs(li, (i, j), li[i][j])

            if rg[i][j] != 0:
                answer2 += 1
                bfs(rg, (i, j), rg[i][j])

    print(answer1, answer2)

if __name__ == "__main__":
    main()