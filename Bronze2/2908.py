import sys

input = sys.stdin.readline


n, m = [int(x[::-1]) for x in input().rstrip().split()]
print(max(n, m))
