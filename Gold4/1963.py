import sys
from collections import deque

input = sys.stdin.readline

dn = (1, 10, 100, 1000, -1, -10, -100, -1000)


def check(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def main():
    n = int(input())
    answers = []

    for _ in range(n):
        start, dest = map(int, input().split())

        def bfs(start):
            que = deque()
            que.append((start, 0))
            visited = [True] * 9000
            while que:
                num, cnt = que.popleft()
                print(num)
                visited[num - 1000] = False
                if num == dest:
                    return cnt
                for i in range(8):
                    new_num = num + dn[i]
                    if (
                        1000 <= new_num < 10000
                        and visited[new_num - 1000]
                        and check(new_num)
                    ):
                        print(new_num)
                        que.append((new_num, cnt + 1))

            return "Impossible"

        answers.append(bfs(start))

    for answer in answers:
        print(answer)


main()
