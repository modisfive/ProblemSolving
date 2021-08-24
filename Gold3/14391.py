import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    matrix = [list(map(int, input().strip())) for _ in range(n)]

    def getNum(arr):
        h, w = len(arr), len(arr[0])

        biggest = 0
        biggest_idx = 0
        answer = 0

        if(h < w):
            for i in range(h):
                if biggest < arr[i][0]:
                    biggest = arr[i][0]
                    biggest_idx = i

            answer = int(''.join(map(str, arr[biggest_idx])))
            del arr[biggest_idx]

        elif(w < h):

        else:

        return answer


main()
