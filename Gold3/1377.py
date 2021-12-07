import sys

input = sys.stdin.readline


# def main():
#     n = int(input())
#     matrix = [int(input()) for _ in range(n)]

#     answer = 1

#     for i in range(n - 1):
#         if matrix[i] > matrix[i + 1]:
#             answer += 1

#     print(answer)


def main():
    n = int(input())
    matrix = [0] + [int(input()) for _ in range(n)]

    changed = False
    for i in range(1, n + 2):
        changed = False
        for j in range(1, n - i + 1):
            if matrix[j] > matrix[j + 1]:
                changed = True
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

        if changed == False:
            print(i)
            break


main()
