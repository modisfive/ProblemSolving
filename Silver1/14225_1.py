import sys

input = sys.stdin.readline

a = [False] * (20 * 100000 + 10)


def go(arr, idx, total):
    global a
    if idx == len(arr):
        a[total] = True
        return

    go(arr, idx + 1, total + arr[idx])
    go(arr, idx + 1, total)


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    go(arr, 0, 0)

    idx = 1
    while True:
        if not a[idx]:
            print(idx)
            return
        idx += 1


main()
