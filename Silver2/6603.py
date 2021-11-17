import sys

input = sys.stdin.readline

answers = []


def add(start, length, curr_arr, arr, cnt):
    if cnt == 6:
        answers.append(curr_arr)
        return

    for i in range(start, cnt + length):
        add(i + 1, length, curr_arr + [arr[i]], arr, cnt + 1)


def main():
    while True:
        arr = list(map(int, input().split()))
        if len(arr) == 1:
            break

        add(0, arr[0] - 6 + 1, [], arr[1:], 0)

        answers.append([])

    for answer in answers[:-1]:
        print(*answer)


if __name__ == "__main__":
    main()
