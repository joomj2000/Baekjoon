import sys

n=int(sys.stdin.readline())

d=[0]*1001
d[0]=1
d[1]=2

for i in range(2,n):
    d[i]=d[i-2]+d[i-1]

print(d[n-1]%10007)