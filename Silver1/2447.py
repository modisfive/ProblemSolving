import sys

input = sys.stdin.readline


def main():
    n = int(input())

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print("***\n* *\n***")


main()
