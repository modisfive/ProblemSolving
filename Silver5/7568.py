import sys

def main():
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    rank = [0 for _ in range(n)]

    def getMaxWIdx():
        MAX = 0
        idx = 0 
        for i, arr in enumerate(matrix):
            if MAX < arr[0] and rank[i] == 0:
                MAX = arr[0]
                idx = i
        return idx

    def getMaxHIdx():
        MAX = 0
        idx = 0 
        for i, arr in enumerate(matrix):
            if MAX < arr[1] and rank[i] == 0:
                MAX = arr[1]
                idx = i
        return idx

    cnt = 1
    while cnt < n+1:
        maxWIdx = getMaxWIdx()
        maxHIdx = getMaxHIdx()
        tmp = []
        if maxWIdx == maxHIdx:
            maxW = matrix[maxWIdx][0]
            maxH = matrix[maxWIdx][1]
            for i, arr in enumerate(matrix):
                if arr[0] == maxW and arr[1] == maxH:
                    tmp.append(i)
        elif maxWIdx != maxHIdx:
            std = matrix[maxWIdx][1]
            for i, arr in enumerate(matrix):
                if arr[1] >= std and rank[i] == 0:
                    tmp.append(i)
        for i in tmp:
            rank[i] = cnt
        cnt += len(tmp)

    print(*rank)

if __name__ == "__main__":
    main()