import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    li = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
    answer = []

    def bfs(num):
        que = deque()
        que.append(num)
        while que:
            for i in li:
                if num in i:
                    tmp = 0             # tmp 자식 num 부모
                    if i[0] == num: tmp = i[1]                   
                    else: tmp = i[0]
                    answer.append([tmp, num])
                    li.remove(i)
                    que.append(tmp)
        
    bfs(1)

    print(answer)
    print(li)

if __name__ == "__main__":
    main()