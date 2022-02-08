from heapq import merge
import sys

input = sys.stdin.readline


def pArr(arr):
    for i in arr:
        print(i)


def merge_sorted(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge(l, r)

    else:
        return arr


def merge(left, right):
    i, j = 0, 0
    h1, h2 = 0, 0
    arr = []

    print()
    print("append")
    print(left)
    print(right)

    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][0]:
            arr.append(left[i])
            i += 1
        if right[j][0] <= left[i][2]:
            arr.append(right[j])
            j += 1
        elif right[j][0] < left[i][2] and left[i][2] < right[j][2]:
            if left[i][1] < right[j][1]:
                arr.append([left[i][0], left[i][1], right[j][0]])
                arr.append(right[j])
                
            else:
                arr.append(left[i])
                arr.append([left[i][2], right[j][1], right[j][2]])
            i += 1
            j += 1
        else:
            if left[i][1] < right[j][1]:
                arr.append(left[i])
            else:
                arr.append([left[i][0], left[i][1], right[j][0]])
                arr.append(right[j])
                arr.append([right[j][2], left[i][1], left[i][2]])
            i += 1
            j += 1

    while j < len(right):
        arr.append(right[j])
        j += 1

    print("result")
    pArr(arr)

    return arr


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    pArr(matrix)

    answer = merge_sorted(matrix)
    # pArr(answer)


"""
    for idx in range(len(answer) - 1):
        print(answer[idx][0], answer[idx][1], end=" ")
        if answer[idx][2] != answer[idx + 1][0]:
            print(answer[idx][2], 0, end=" ")

    print(answer[-1][0], answer[-1][1], answer[-1][2], 0)
"""


main()
