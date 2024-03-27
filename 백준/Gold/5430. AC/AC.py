import sys
from collections import deque
N = int(sys.stdin.readline())

deque = deque([])
for _ in range(N):
    error=0
    cnt=0
    command=sys.stdin.readline()
    n=int(sys.stdin.readline())
    number=sys.stdin.readline()
    number=number.replace('[','').replace(']','').replace('\n','')
    if n!=0:
        try:
            number_list=[int(x) for x in number.split(',')]
        except:
            print('error')
            continue
    
        for j in number_list:
            if j!=',' and j!=']' and j!='[' and j!='\n':
                deque.append(int(j))
    for i in command:
        if i=='R':
            cnt+=1
        elif i=='D':
            if len(deque)==0:
                print('error')
                error=1
                break
            if cnt%2==0:
                deque.popleft()
            else:
                deque.pop()

    if error==0:
        print('[',end='')
        while len(deque)>1:
            if cnt % 2 == 0:
                print(deque.popleft(),end=',')
            else:
                print(deque.pop(),end=',')
        if(len(deque)==1):
            print(deque.pop(),end='')
        print(']')