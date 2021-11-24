import sys

input = sys.stdin.readline


def func(num1, num2):
    if num1 < num2:
        return (num1 * 2, num2 - num1)
    else:
        return (num1 - num2, num2 + 2)


def main():
    a, b, c = map(int, input().split())

    




main()
