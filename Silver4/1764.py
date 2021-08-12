import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    tmp = []
    answer = []

    for _ in range(n):
        name = input().strip()
        tmp.append(name)
    
    for _ in range(m):
        name = input().strip()
        if name in tmp:
            answer.append(name)

    answer.sort()

    print(len(answer))
    
    for name in answer:
        print(name, end='\n')

if __name__ == "__main__":
    main()