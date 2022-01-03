import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())

    if k == 0:
        answer = "B" + "A" * (n - 1)
    else:
        n1, n2 = 0, 0
        flag = 0
        for num in range(1, k + 1):
            if k % num == 0:
                num2 = k // num
                if (num + num2) <= n:
                    n1, n2 = num, num2
                    flag = 1
                    break
        if flag:
            answer = "B" * (n - n1 - n2) + "A" * n1 + "B" * n2
        else:
            answer = -1

    print(answer)


main()
