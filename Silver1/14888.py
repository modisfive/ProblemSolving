import sys
from itertools import permutations

input = sys.stdin.readline


def main():
    n = int(input())
    num = list(map(int, input().split()))
    calc = list(map(int, input().split()))

    calc_list = []
    for i in range(4):
        for _ in range(calc[i]):
            calc_list.append(i)

    nPr = list(permutations(calc_list, n - 1))

    def doCalc(num1, num2, act):
        if act == 0:
            return num1 + num2
        elif act == 1:
            return num1 - num2
        elif act == 2:
            return num1 * num2
        else:
            if num1 < 0:
                return -(-num1 // num2)
            else:
                return num1 // num2

    answer = []

    for arr in nPr:
        num1 = num[0]
        for i in range(n - 1):
            num2 = num[i + 1]
            act = arr[i]
            num1 = doCalc(num1, num2, act)
        answer.append(num1)

    print(max(answer))
    print(min(answer))


if __name__ == "__main__":
    main()
