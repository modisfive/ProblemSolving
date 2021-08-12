import sys   

def main():
    num = int(sys.stdin.readline())
    answer = [0]*10
    
    length = len(str(num))

    for i in answer:
        if i == 0:
            for k in range(1, length):
                answer[i] += (10 ** k) * (num // (10 ** (k+1)))

    print(answer[0])






if __name__ == "__main__":
    main()