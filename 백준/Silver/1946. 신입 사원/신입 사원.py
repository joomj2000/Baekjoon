import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    test = []
    for _ in range(N):
        test1, test2=map(int, sys.stdin.readline().split())
        test.append([test1, test2])
    test=sorted(test)
    min=test[0][1]
    cnt=1
    for test1,test2 in test:
        if(test2<min):
            cnt+=1
            min=test2

    print(cnt)
