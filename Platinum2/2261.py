import sys

input = sys.stdin.readline


def getDistance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def brute_force(points, start, end):
    answer = 9999
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            tmp_d = getDistance(points[i], points[j])
            if tmp_d < answer:
                answer = tmp_d

    return answer


def solve(points, start, end):
    n = end - start + 1
    if n <= 3:
        return brute_force(points, start, end)

    mid = (start + end) // 2
    left = solve(points, start, mid)
    right = solve(points, mid + 1, end)
    answer = min(left, right)
    tmp = []
    for idx in range(start, end + 1):
        d = points[idx][0] - points[mid][0]
        if d * d < answer:
            tmp.append(points[idx])
    tmp.sort(key=lambda x: x[1])

    for i in range(len(tmp) - 1):
        for j in range(i + 1, len(tmp)):
            y = tmp[i][1] - tmp[j][1]
            if y * y < answer:
                d = getDistance(tmp[i], tmp[j])
                if d < answer:
                    answer = d
            else:
                break

    return answer


def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    points.sort(key=lambda x: x[0])

    print(solve(points, 0, n - 1))


main()
