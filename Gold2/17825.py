import sys
from copy import deepcopy

input = sys.stdin.readline


def main():
    results = list(map(int, input().split()))
    matrix = [
        [x for x in range(41) if x % 2 == 0],
        [10, 13, 16, 19, 25, 30, 35, 40],
        [20, 22, 24, 25, 30, 35, 40],
        [30, 28, 27, 26, 25, 30, 35, 40],
    ]
    horses = [(0, 0), (0, 0), (0, 0), (0, 0)]

    answer = 0

    def roll(horses, idx, result):
        status = deepcopy(horses)
        path, index = status[idx]
        dest = 0
        tmp = tuple()
        if index + result < len(matrix[path]):

            if path == 0:
                tmp_dest = matrix[0][index + result]
                if tmp_dest % 10 == 0 and tmp_dest != 40:
                    tmp = (tmp_dest // 10, 0)
                else:
                    tmp = (0, index + result)
            else:
                tmp = (path, index + result)

            if tmp not in status:
                status[idx] = tmp
                dest = matrix[tmp[0]][tmp[1]]

        else:
            del status[idx]

        print(status)

        return status, dest

    def solve(horses, tmp_sum, cnt):
        nonlocal answer
        if cnt == 10 or len(horses) == 0:
            answer = max(answer, tmp_sum)
            return

        for idx in range(len(horses)):
            status, dest = roll(horses, idx, results[cnt])
            solve(status, tmp_sum + dest, cnt + 1)

    solve(horses, 0, 0)

    print(answer)


main()
