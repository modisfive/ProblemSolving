import sys

input = sys.stdin.readline

answer = 0


def go(arr, goal, idx, total):
    global answer
    if idx == len(arr):
        if total == goal:
            answer += 1
        return

    go(arr, goal, idx + 1, total + arr[idx])
    go(arr, goal, idx + 1, total)


def main():
    global answer
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    go(arr, s, 0, 0)

    if s == 0:
        answer -= 1
    print(answer)


main()
