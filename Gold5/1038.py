import sys
input = sys.stdin.readline

def main():
    n = int(input())

    def check(num):
        matrix = [int(x) for x in str(num)]
        if len(matrix) == 1: 
            if num == 0: return False
            else : return True
        for i in range(len(matrix)-1):
            if matrix[i] > matrix[i+1]:
                continue 
            else: return False
        return True
    

    answer = 0
    cnt = 0
    while True:
        if check(answer): cnt += 1
        if cnt == n: break
        answer += 1

    print(answer)


if __name__ == "__main__": 
    main()