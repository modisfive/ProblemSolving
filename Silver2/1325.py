import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        matrix[b].append(a)

    res = [0]*(n+1)
    MAX = 0

    def bfs(num):
        nonlocal MAX
        if not res[num]:
            que = deque()
            que.append(num)
            while que:
                number = que.popleft()
                if res[number]: res[num] += res[number]
                elif not matrix[number]: continue
                else: 
                    for i in matrix[number]:
                        que.append(i)
            MAX = max(MAX, res[num])
    
    answer = []

    for i in range(1, n+1):
        bfs(i)

    for idx, value in enumerate(res):
        if MAX == value:
            answer.append(idx)

    print(*answer)

if __name__ == "__main__":
    main()