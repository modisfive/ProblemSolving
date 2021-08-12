import sys

path = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)], 
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (-1, 0)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (1, 0), (2, 0), (0, -1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 2), (0, 1), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 0)]
]

def main():
    m, n = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    candidates = []

    for i in range(m):
        for j in range(n):
            for arr1 in path:
                tmp = 0
                stop = True
                for arr2 in arr1:
                    if 0<=i+arr2[0]<m and 0<=j+arr2[1]<n:
                        tmp += matrix[i+arr2[0]][j+arr2[1]]
                        stop = False
                    if stop: break
                if stop: continue
                else: candidates.append(tmp)

    print(max(candidates))

if __name__ == "__main__":
    main()