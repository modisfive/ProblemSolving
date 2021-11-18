import sys

input = sys.stdin.readline

candidates = set()


def add(cnt, length, arr, curr_cnt, start, result):
    if cnt == curr_cnt:
        candidates.add(result)
        return

    for idx in range(start, length - (cnt - curr_cnt) + 1):
        add(cnt, length, arr, curr_cnt + 1, idx + 1, result + arr[idx])


def main():
    length = int(input())
    arr = list(map(int, input().split()))

    candidates.update(arr)

    if length == 1:
        print(2 if arr[0] == 1 else 1)
        return

    for cnt in range(2, length + 1):
        add(cnt, length, arr, 0, 0, 0)

    arr_candidates = list(candidates)

    # print(arr_candidates)

    for idx in range(len(arr_candidates)):
        if arr_candidates[idx] != idx + 1:
            print(idx + 1)
            return

    print(max(arr_candidates) + 1)


main()
