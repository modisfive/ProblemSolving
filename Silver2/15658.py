import sys

input = sys.stdin.readline

results = ()

def setOp(length, remain_op, operators):
    if length == len(operators):
        results.add(operators)
        return 
    
    operator = ["+", "-", "*", "/"]

    for idx in range(4):
        
            setOp(length, remain_op, operators+[operator[idx]])



def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    remain_op = list(map(int, input().split()))


    print(result)


main()
