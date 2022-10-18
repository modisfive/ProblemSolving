import sys

input = sys.stdin.readline


n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

pre_ops = input().strip().split()

length = 0
ops = []
for op in pre_ops:
    if len(ops) != 0 and ops[-1] == op:
        length += 1

        if length == 2 and op in "12":
            ops.pop()
        elif length == 4 and op in "3456":
            for _ in range(3):
                ops.pop()
        else:
            ops.append(op)
    elif len(ops) != 0 and (
        (ops[-1] == "5" and op == "6") or (ops[-1] == "6" and op == "5")
    ):
        ops.pop()
    else:
        length = 1
        ops.append(op)


def op_1(array):
    array = array[::-1]


def op_2(array):
    array = [array[i][::-1] for i in range(n)]


def op_3(array):
    array = [list(arr)[::-1] for arr in zip(*array)]


def op_4(array):
    array = [list(arr) for arr in zip(*array)][::-1]


def op_5(array):
    h = len(array)
    w = len(array[0])
    h_mid = h // 2
    w_mid = w // 2
    result = [[0] * h for _ in range(w)]
    for i in range(h_mid):
        for j in range(w_mid):
            result[i][j + w_mid] = array[i][j]
        for j in range(w_mid, w):
            result[i + h_mid][j] = array[i][j]
    for i in range(h_mid, h):
        for j in range(w_mid, w):
            result[i][j - w_mid] = array[i][j]
        for j in range(w_mid):
            result[i - h_mid][j] = array[i][j]
    array = result


def op_6(array):
    h = len(array)
    w = len(array[0])
    h_mid = h // 2
    w_mid = w // 2
    result = [[0] * w for _ in range(h)]
    for i in range(h_mid):
        for j in range(w_mid):
            result[i + h_mid][j] = array[i][j]
        for j in range(w_mid, w):
            result[i][j - w_mid] = array[i][j]
    for i in range(h_mid, h):
        for j in range(w_mid):
            result[i][j + w_mid] = array[i][j]
        for j in range(w_mid, w):
            result[i - h_mid][j] = array[i][j]
    array = result


operators = {
    "1": op_1,
    "2": op_2,
    "3": op_3,
    "4": op_4,
    "5": op_5,
    "6": op_6,
}


for op in ops:
    operators[op](array)

for arr in array:
    print(*arr)
