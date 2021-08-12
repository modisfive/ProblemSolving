import sys

def main():
    day = int(sys.stdin.readline())
    matrix = [[]]
    for i in range(day):
        a, b = map(int, sys.stdin.readline().split())
        matrix.append([a, b])

    payment = []

    def dfs(cur, total):        
        pay = total + matrix[cur][1]    
        stop = True
        
        for i in range(cur + matrix[cur][0], day+1):
            if i + matrix[i][0] - 1 < day+1:
                dfs(i, pay)
                stop = False
        
        if stop == True:
            payment.append(pay)

    for i in range(1, day+1):
        if i + matrix[i][0] - 1 < day+1:
            dfs(i, 0)

    if payment:                                     
        print(max(payment))                         # 모든 일의 종료일이 day를 오버해서 일을 하나도 못하고 퇴사하는 경우
    else: print(0)

if __name__ == "__main__":
    main()
        