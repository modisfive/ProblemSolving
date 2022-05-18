import sys

input = sys.stdin.readline


def main():
    n = int(input())
    balls = []

    for idx in range(n):
        color, size = map(int, input().split())
        balls.append([color, size, idx])

    total = 0
    balls.sort(key=lambda x: x[1])
    colors = [0] * (n + 1)
    points = [0] * n

    j = 0
    for i in range(n):
        pivot = balls[i]
        ball = balls[j]

        while ball[1] < pivot[1]:
            total += ball[1]
            colors[ball[0]] += ball[1]
            j += 1
            ball = balls[j]

        points[pivot[2]] = total - colors[pivot[0]]

    for p in points:
        print(p)


main()
