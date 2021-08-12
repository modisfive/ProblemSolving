import sys
input = sys.stdin.readline
from collections import deque

def pArr(arr):
    for i in arr:
        print(i)


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    answer = []

    def goUp():
        for i in range(n):
            que = deque()
            for j in range(n):       
                if matrix[j][i] != 0:
                    que.append(matrix[j][i])
            idx = 0
            tmp1 = que.popleft()
            while que:
                tmp2 = que.popleft()
                if tmp1 == tmp2: 
                    matrix[idx][n] = tmp1*2
                    idx += 1
                    tmp1 = que.popleft()
                else: 
                    matrix[idx][n] = tmp1
                    tmp1 = tmp2
                    idx += 1
            for j in range(idx+1, n):
                matrix[j][n] = 0                

    pArr(matrix)
    goUp()
    pArr(matrix)



if __name__ == "__main__":
    main()