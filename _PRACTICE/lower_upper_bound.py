"""
    lower bound는 찾고자 하는 숫자가 처음으로 나오는 인덱스를 찾는다.
    uppper bound는 찾고자 하는 숫자보다 큰 값이 처음으로 나오는 인덱스를 찾는다.
"""


arr = [1, 1, 1, 2, 2, 3, 4, 4, 4]


def lower_bound(arr, k):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if k <= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left


def upper_bound(arr, k):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if k < arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left


print(lower_bound(arr, 2))
print(upper_bound(arr, 2))
