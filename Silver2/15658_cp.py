import sys

input = sys.stdin.readline

numbers = list()
length = 0
results = []


def calc(idx, acc, plus, minus, mul, div):
    if idx == length:
        results.append(acc)

    if plus > 0:
        calc(idx + 1, acc + numbers[idx], plus - 1, minus, mul, div)
    if minus > 0:
        calc(idx + 1, acc - numbers[idx], plus, minus - 1, mul, div)
    if mul > 0:
        calc(idx + 1, acc * numbers[idx], plus, minus, mul - 1, div)
    if div > 0:
        calc(idx + 1, acc // numbers[idx], plus, minus, mul, div - 1)


def main():
    global numbers, length
    length = int(input())
    numbers = list(map(int, input().split()))
    plus, minus, mul, div = map(int, input().split())


main()
