import sys

def backtracking():
    if len(num)==M:
        print(" ".join(map(str,num)))
        return
    for i in range(1,N+1):
        if i not in num:
            num.append(i)
            backtracking()
            num.pop()

N,M=map(int, sys.stdin.readline().split())
num=[]
backtracking()