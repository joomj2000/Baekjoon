import sys

N,r,c=map(int,sys.stdin.readline().split())

num=0
while(N>0):
    N -= 1
    target=2**(N)
    if r<target and c<target : #1
        num=num
    elif r<target and c >=target : #2
        num+=target * target
        c-=(2**N)
    elif r>=target and c < target : #3
        num += target * target*2
        r-=(2**N)
    elif r>=target and c >=target : #4
        num +=target * target * 3
        c -= (2 ** N)
        r -= (2 ** N)

print(num)

