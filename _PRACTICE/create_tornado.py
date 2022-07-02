"""
    회전하는 토네이도 만들기 (ex. boj 21611)
    n은 홀수
"""


def create(n):
    x, y = n // 2, n // 2
    graph = [[0] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]  # 좌 하 우 상
    dy = [0, 1, 0, -1]
    depth = 0
    num = 1

    while True:
        for i in range(4):
            if i % 2 == 0:
                depth += 1
            for _ in range(depth):
                x += dx[i]
                y += dy[i]
                graph[y][x] = num
                num += 1
                if x == 0 and y == 0:
                    return graph


graph = create(5)

for row in graph:
    print(row)
