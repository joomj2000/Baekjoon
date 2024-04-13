import sys

def backtracking():
    if len(num)==6:
        print(" ".join(map(str,num)))
        return
    for i in num_list:
        if i not in num:
            if len(num)==0 or num[-1]<i:
                num.append(i)
                backtracking()
                num.pop()


while(True):
    num_list=[]
    command=list(map(int, sys.stdin.readline().strip().split()))
    N=command[0]
    if N==0:
        break

    for i in range(1,N+1):
        num_list.append(command[i])
    num=[]
    backtracking()
    print('')