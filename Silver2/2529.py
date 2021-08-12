import sys
input = sys.stdin.readline
import itertools

def main():
    n = int(input())
    matrix = input().split()

    def toNum(arr):
        return ''.join(arr)


    candidates = list(itertools.permutations([str(x) for x in range(10)], n+1))
    result = []
    
    for arr in candidates:
        stop = False
        for i in range(n):
            if matrix[i] == '<':
                if int(arr[i]) < int(arr[i+1]): continue
                else:
                    stop = True
                    break
            else:
                if int(arr[i]) > int(arr[i+1]): continue
                else: 
                    stop = True
                    break
        if stop: continue
        result.append(toNum(arr))

    print(result[-1])
    print(result[0])
        

if __name__ == "__main__":
    main()