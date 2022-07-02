"""
    이차원 배열 시계 방향, 반시계 방향 90도 회전하기
"""


def pArr(arr):
    for row in arr:
        print(row)


# 시계 방향 90도 회전
def rotate(graph):
    return [list(arr)[::-1] for arr in zip(*graph)]


# 반시계 방향 90도 회전
def rotate_reverse(graph):
    return [list(arr) for arr in zip(*graph)][::-1]


graph = [[0] * 5 for _ in range(5)]
num = 1

for i in range(5):
    for j in range(5):
        graph[i][j] = num
        num += 1

pArr(graph)

print("=" * 30)

graph = rotate(graph)
pArr(graph)

print("=" * 30)

graph = rotate_reverse(graph)
pArr(graph)
