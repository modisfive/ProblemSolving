import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(input().strip()) for _ in range(n)]
    
    answer = 0
    def check():
        cnt = 0
        for i in range(n):
            tmp1 = 1
            tmp2 = 1
            for j in range(n):
                if matrix[i][j] == matrix[i][j+1]:
                    tmp1 += 1
                else: 
                    cnt = max(cnt, tmp1)
                    tmp1 = 1

                if matrix[j][i] == matrix[j+1][i]:
                    tmp2 += 1
                else: 
                    cnt = max(cnt, tmp2)
                    tmp2 = 1    
        return cnt

    answer = check()

    def swap(num1, num2):
        tmp = num1
        num1 = num2
        num2 = tmp

    for i in range(n):
        for j in range(n-1):
            swap(matrix[i][j], matrix[i][j+1])
            answer = max(answer, check())
            swap(matrix[i][j], matrix[i][j+1])
    for i in range(n-1):
        for j in range(n):
            swap(matrix[i][j], matrix[i+1][j])
            answer = max(answer, check())
            swap(matrix[i][j], matrix[i+1][j])

    print(answer)





if __name__ == "__main__":
    main()