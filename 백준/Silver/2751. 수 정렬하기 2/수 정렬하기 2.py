import sys
N = int(sys.stdin.readline())
A=[]
for _ in range(N):
    A.append(int(sys.stdin.readline()))
result=sorted(A)
for i in range(N):
    print(result[i])