import sys
import math
from collections import deque

input = sys.stdin.readline

ladders = list()


def calc_bw(start, end=100):
    return math.ceil((end - start) / 6)


def func(start):
    global ladders

    result = 999999
    que = deque()
    que.append(start)

    while que:
        curr, cnt = que.popleft()
        if cnt > result:
            continue
        bw_end = calc_bw(curr)
        if bw_end + cnt < result:
            result = bw_end + cnt
        for ladder in ladders:
            if curr < ladder[0]:
                que.append((ladder[1], cnt + calc_bw(curr, ladder[0])))
    return result


def main():
    global ladders, answer

    n, m = map(int, input().split())
    for _ in range(n + m):
        ladders.append(tuple(map(int, input().split())))

    ladders.sort(key=lambda x: x[0])

    answer = func((1, 0))

    print(answer)


main()
