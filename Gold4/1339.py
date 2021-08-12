import sys

def main():
    n = int(sys.stdin.readline())
    li = [sys.stdin.readline()[:-1] for _ in range(n)]
    
    fre = [0 for _ in range(26)]

    for i in li:
        for idx, j in enumerate(list(i)[::-1]):
            fre[ord(j)-ord('A')] += 10 ** idx

    fre.sort(reverse=True)

    answer = 0

    for i in range(9, 0, -1):
        answer += i * fre[9-i]
    
    print(answer)


if __name__ == "__main__":
    main()