import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def main():
    num = int(input())

    def fac(num):
        if num == 1:
            return 1
        else:
            return num*fac(num-1)

    tmp = fac(num)

    answer = [x for x in str(tmp)]
    cnt = 0

    for idx in range(len(answer)-1, -1, -1):
        if answer[idx] != '0':
            break
        else: cnt += 1

    print(cnt)

main()