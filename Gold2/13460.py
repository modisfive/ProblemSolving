import sys
input = sys.stdin.readline
from collections import deque

blue = (0, 0)   # (세로, 가로)
red = (0, 0)
goal = (0, 0)

def pArr(arr):
    for i in arr:
        print(i)

def main():
    global red, blue, goal
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'B': blue = (i, j) 
            if matrix[i][j] == 'R': red = (i, j)
            if matrix[i][j] == 'O': goal = (i, j)

    def goUp(pos):
        y, x = pos
        tmp = y
        cnt = 0
        while matrix[tmp-1][x] != '#':
            tmp -= 1
            if matrix[y][tmp] == '.': cnt += 1
        return (y-cnt, x)

    def goRight(pos):
        y, x = pos
        tmp = x
        cnt = 0
        while matrix[y][tmp+1] != '#':
            tmp += 1
            if matrix[y][tmp] == '.': cnt += 1
        return (y, x+cnt)

    def goLeft(pos):
        y, x = pos
        tmp = x
        cnt = 0
        while matrix[y][tmp-1] != '#':
            tmp -= 1
            if matrix[y][tmp] == '.': cnt += 1
        return (y, x-cnt)
    
    def goDown(pos):
        y, x = pos
        tmp = y
        cnt = 0
        while matrix[tmp+1][x] != '#':
            tmp += 1
            if matrix[tmp][x] == '.': cnt += 1
        return (y+cnt, x)

    def actSync(act):
        global red, blue
        red = act(red)
        blue = act(blue)
    
    pArr(matrix)
    actSync(goDown)
    print()
    pArr(matrix)

if __name__ == "__main__":
    main()