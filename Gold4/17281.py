import sys
input = sys.stdin.readline
from collections import deque
import itertools

def main():
    totalInning = int(input())
    expected = [list(map(int, input().split())) for _ in range(totalInning)]

    totalScore = 0

    def calcCurr():
        nonlocal curr
        if curr == 8:
            curr = 0
        else: curr += 1

    def hit(num):
        nonlocal score
        for i in range(num):
            if i == 0: base.append(1)
            else: base.append(0)
            score += base.popleft()
        
    sequence = list(itertools.permutations(range(1, 9)))

    for i in range(len(sequence)):
        tmp = list(sequence[i])
        tmp.insert(3, 0)
        sequence[i] = tmp

    for batter in sequence:
        score = 0
        curr = 0
        base = deque([0, 0, 0])
        for i in range(totalInning):
            out = 0
            while out < 3:
                while True:
                    if expected[i][batter[curr]] == 0:
                        calcCurr()
                        out += 1
                        break 
                    else: 
                        hit(expected[i][batter[curr]])
                        calcCurr()
            base.clear()
        totalScore = max(totalScore, score)

    print(totalScore)


if __name__ == "__main__":
    main()