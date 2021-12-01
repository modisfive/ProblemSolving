import sys
import copy


input = sys.stdin.readline


def main():
    n = int(input())
    matrix = list(map(int, input().strip()))
    goal = list(map(int, input().strip()))

    def flip(arr, idx):
        if idx == 0:
            scope = (idx, idx + 1)
        elif idx == n - 1:
            scope = (idx - 1, idx)
        else:
            scope = (idx - 1, idx, idx + 1)

        for i in scope:
            arr[i] = 1 - arr[i]

    def change(arr):
        cnt = 0
        for i in range(n - 1):
            if arr[i] != goal[i]:
                cnt += 1
                flip(arr, i + 1)
        if arr[-1] != goal[-1]:
            return 0
        else:
            return cnt

    result_1 = change(copy.deepcopy(matrix))
    flip(matrix, 0)
    result_2 = change(copy.deepcopy(matrix))
    if result_2 != 0:
        result_2 += 1

    if result_1 and result_2:
        answer = min(result_1, result_2)
    elif result_1:
        answer = result_1
    elif result_2:
        answer = result_2
    else:
        answer = -1

    print(answer)


main()
