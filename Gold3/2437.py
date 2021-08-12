import sys
from itertools import combinations

def main():
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    answer = 1
    
    for i in range(1, n+1):
        for j in combinations(li, i):
            if answer 
    

if __name__ == "__main__":
    main()