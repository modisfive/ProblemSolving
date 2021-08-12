import sys
input = sys.stdin.readline

def main():
    matrix = [[x for x in range(41) if not x%2],
        [10, 13, 16, 19, 25, 30, 35, 40],
        [20, 22, 24, 25, 30, 35, 40],
        [30, 28, 27, 26, 25, 30, 35, 40]
    ]
    

    dice = list(map(int, input().split()))
    unit = [(0,0), (0,0), (0,0), (0,0), (0,0)]
    answer = []

    def roll(piece, num):
        curr = unit[piece]
        unit[piece] = (curr[0], curr[1]+num)
        if matrix[curr[0]][curr[1]] % 10 == 0:
            unit[piece] = (matrix[curr[0]][curr[1]] // 10, num)         
        return matrix[unit[piece][0]][unit[piece][1]]

    def rollAll(tmpSum, piece, cnt):
        nonlocal answer
        if cnt == 10: 
            answer = max(answer, tmpSum)
            return
            
        num = dice[cnt]
        curr = unit[piece]

        if curr == (-1, -1): return
        if curr[1]+num > len(matrix[curr[0]]): 
            unit[piece] = (-1, -1)
            return

        tmp = (curr[0], curr[1]+num)
        if matrix[curr[0]][curr[1]+num] % 10 == 0:
            tmp = (matrix[curr[0]][curr[1]] // 10, num)
        if tmp in unit: return 

        score = roll(piece, num)
        for i in range(5):
            rollAll(tmpSum+score, i, cnt+1)

    for i in range(5):
        rollAll(0, i, 0)

    print(answer)

if __name__ == "__main__":
    main()