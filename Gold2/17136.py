import sys
input = sys.stdin.readline

def main():
    matrix = [list(map(int, input().split())) for _ in range(10)]

    usable = [0]+[5]*5

    num = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1: num += 1

    answer = 0
    def colorPaper(paper, counter):
        nonlocal answer
        
        if counter == num: 
            answer = min(answer, paper)
            return 
        if paper>answer:
            return
    

        for length in range(5, 0, -1):
            for i in range(10):
                for j in range(10):
                    if matrix[i][j] == 1 and i+length-1 < 10 and j+length-1 < 10:
                        stop = False
                        for n in range(i, i+length):
                            for m in range(j, j+length):
                                if matrix[n][m] != 1:
                                    stop = True
                                    break
                            if stop: break
                        if stop: continue
                        
                        for n in range(i, i+length):
                            for m in range(j, j+length):
                                matrix[n][m] = -1
                        usable[length] -= 1

                        colorPaper(paper+1, counter+length*length)

                        for n in range(i, i+length):
                            for m in range(j, j+length):
                                matrix[n][m] = 1
                        usable[length] += 1
                        
    
    colorPaper(0, 0)
    print(usable)

    


if __name__ == "__main__":
    main()