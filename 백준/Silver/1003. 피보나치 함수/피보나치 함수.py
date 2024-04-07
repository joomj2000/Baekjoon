import sys
d=[0]*41
# def fibonacci(n):
# #     if n==0:
# #         #print("0")
# #         global zero
# #         zero+=1
# #         return 0
# #     if n==1 :
# #         global one
# #         one += 1
# #         return 1
# #     if d[n]!=0:
# #         return d[n]
# #     d[n]=fibonacci(n-1)+fibonacci(n-2)
# #     return d[n]

d=[0]*41
d[1]=1
d[2]=1


T = int(sys.stdin.readline())

zero = 0
one = 0
for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(3,N+1):
        d[i]=d[i-1]+d[i-2]
    if N==0:
        print('1',end=' ')
    else:
        print(d[N-1],end=' ')
    print(d[N])
   # print(zero, one)
    zero = 0
    one = 0