import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())

    answer = []

    for _ in range(n):
        v, e = map(int, sys.stdin.readline().split())
        matrix = [[] for _ in range(v+1)]

        for _ in range(e):
            a, b = map(int, sys.stdin.readline().split())
            matrix[a].append(b)
            matrix[b].append(a)
        
        color = [None]*(v+1)
        
        def bfs(start):
            que = deque()
            que.append(start)
            color[start] = 'X'
            while que:
                tmp = que.popleft()
                if color[tmp] == 'X':
                    for i in matrix[tmp]:
                        if color[i] == None:
                            que.append(i)
                            color[i] = 'Y'
                        elif color[i] == 'X': 
                            answer.append('NO')
                            return
                else:
                    for i in matrix[tmp]:
                        if color[i] == None:
                            que.append(i)
                            color[i] = 'X'
                        elif color[i] == 'Y': 
                            answer.append('NO')
                            return

            answer.append('YES')

        bfs(1)

    for i in answer:
        print(i)
    
if __name__ == "__main__":
    main()