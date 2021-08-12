import sys
input = sys.stdin.readline
from collections import deque

def main():
    f, curr, dest, up, down = map(int, input().split())

    cnt = 0
    if curr < dest: 
        cnt = (dest-curr)//up
        curr += cnt*up
    else:
        cnt = (curr-dest)//down
        curr -= cnt*down

    
            
