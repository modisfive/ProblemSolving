from collections import deque


def pArr(arr):
    for row in arr:
        print(row)


def rotate_surface(arr, top_left, bottom_right):
    que = deque()

    a, b = top_left  # y1, x1
    c, d = bottom_right  # y2, x2

    for i in range(d - b):
        que.append(arr[a][b + i])
    for i in range(c - a):
        que.append(arr[a + i][d])
    for i in range(d - b):
        que.append(arr[c][d - i])
    for i in range(c - a):
        que.append(arr[c - i][b])

    que.rotate(1)

    for i in range(d - b):
        arr[a][b + i] = que.popleft()
    for i in range(c - a):
        arr[a + i][d] = que.popleft()
    for i in range(d - b):
        arr[c][d - i] = que.popleft()
    for i in range(c - a):
        arr[c - i][b] = que.popleft()

    return arr


columns = 5
rows = 5

arr = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]

pArr(arr)

print("=" * 30)

arr = rotate_surface(arr, (1, 1), (3, 3))

pArr(arr)
