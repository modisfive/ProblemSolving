import sys
input = sys.stdin.readline

def countZero(arr):
    cnt = 0
    for arr1 in arr:
        cnt += arr1.count(0)
    return cnt

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    cam = [[] for _ in range(6)]
    block = []
    for i in n:
        for j in m:
            if matrix[i][j] == 1: cam[1].append((i, j))
            if matrix[i][j] == 2: cam[2].append((i, j))
            if matrix[i][j] == 3: cam[3].append((i, j))
            if matrix[i][j] == 4: cam[4].append((i, j))
            if matrix[i][j] == 5: cam[5].append((i, j))
            if matrix[i][j] == 6: block.append((i, j))

    answer = []

    for p in cam[5]:
        y, x = p
        for i in range(x+1, n):
            if matrix[y][i] == 6: break
            elif matrix[y][i] != 0: continue
            else: matrix[y][i] = '#'
        for i in range(x-1, -1, -1):
            if matrix[y][i] == 6: break
            elif matrix[y][i] != 0: continue
            else: matrix[y][i] = '#'
        
    




if __name__ == "__main__":
    main()