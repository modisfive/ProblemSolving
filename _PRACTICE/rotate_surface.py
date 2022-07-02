from collections import deque


def pArr(arr):
    for row in arr:
        print(row)


def rotate_surface(arr, top_left, bottom_right):
    que = deque()

    a, b = top_left
    c, d = bottom_right

    for x in range(d - b):
        que.append(arr[a][b + x])
    for y in range(c - a):
        que.append(arr[a + y][d])
    for z in range(d - b):
        que.append(arr[c][d - z])
    for k in range(c - a):
        que.append(arr[c - k][b])

    que.rotate(1)

    for x in range(d - b):
        arr[a][b + x] = que.popleft()
    for y in range(c - a):
        arr[a + y][d] = que.popleft()
    for z in range(d - b):
        arr[c][d - z] = que.popleft()
    for k in range(c - a):
        arr[c - k][b] = que.popleft()

    return arr


columns = 5
rows = 5

arr = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]

pArr(arr)

print("=" * 30)

arr = rotate_surface(arr, (1, 1), (3, 3))

pArr(arr)
