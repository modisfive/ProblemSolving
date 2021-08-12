import sys

def main():
    answer = [0]*10
    num = int(sys.stdin.readline())
    for i in range(1, num+1):
        for idx in [int(x) for x in str(i)]:
            answer[idx] += 1

    print(answer)

main()
