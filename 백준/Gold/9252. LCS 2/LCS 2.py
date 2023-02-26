import sys

input = sys.stdin.readline


string1 = input().strip()
string2 = input().strip()

n = len(string1)
m = len(string2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

length = dp[n][m]

string = ""

i, j = n, m
while len(string) < length:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        string += string1[i - 1]
        i -= 1
        j -= 1

string = string[::-1]
print(length)
print(string)