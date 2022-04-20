import sys

input = sys.stdin.readline


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    def f(x):
        return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

    answer = 0

    if (
        (x1 == x2 and x2 == x3)
        or (y1 == y2 and y2 == y3)
        or ((y2 - y1) / (x2 - x1) == (y3 - y2) / (y2 - y1))
    ):
        answer = 0
    elif x1 == x2:
        if x1 < x3:
            answer = -1
        elif x1 > x3:
            answer = 1
    elif x1 < x2:
        if y3 > f(x3):
            answer = 1
        elif y3 < f(x3):
            answer = -1
    elif x1 > x2:
        if y3 > f(x3):
            answer = -1
        elif y3 < f(x3):
            answer = 1

    print(answer)


main()
