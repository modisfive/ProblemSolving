# import sys

# input = sys.stdin.readline


# n = int(input())
# q = n**0.5

# if q % 1 == 0:
#     print(int(q))
# else:
#     print(int(q) + 1)

import sys

input = sys.stdin.readline


n = int(input())
start, end = 0, n

while start <= end:
    mid = (start + end) // 2
    if mid**2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)
