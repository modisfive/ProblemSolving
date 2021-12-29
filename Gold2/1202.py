import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    gems = [list(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    occupied = [0] * (max(bags) + 1)
    bags.sort()

    def getBag(vol):
        diff = 9999
        bag = -1
        for b in bags:
            if vol <= b and abs(b - vol) < diff:
                diff = abs(b - vol)
                bag = b
        return bag

    for gem in gems:
        vol = gem[0]
        price = gem[1]
        bag = getBag(vol)
        if bag == -1:
            continue
        if (occupied[bag] == 0) or (occupied[bag] < price):
            occupied[bag] = price

    print(sum(occupied))


main()
