import sys

def backtracking():
    if len(num)==M:
        print(" ".join(map(str,num)))
        return
    for i in num_list:
        if i not in num:
            num.append(i)
            backtracking()
            num.pop()

N,M=map(int, sys.stdin.readline().split())

num_list=list(map(int, sys.stdin.readline().strip().split()))
num_list.sort()
num=[]
backtracking()
