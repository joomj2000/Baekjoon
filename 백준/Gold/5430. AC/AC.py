import sys
from collections import deque
N = int(sys.stdin.readline())

deque = deque([])
for _ in range(N):
    error=0
    cnt=0
    command=sys.stdin.readline()
    #print('command=',command)
    n=int(sys.stdin.readline())
    #number_list=[]
    number=sys.stdin.readline()
    number=number.replace('[','').replace(']','').replace('\n','')
    # if command.count('D')>n:
    #     print('error')

    # if n!=1 and ',' not in number: #여기 수정 1 R 1일때 이상함
    #     print('error')
    #     continue
    if n!=0:
        try:
            number_list=[int(x) for x in number.split(',')]
        except:
            print('error')
            continue
    #print('number=',number)
        for j in number_list:
            if j!=',' and j!=']' and j!='[' and j!='\n':
                deque.append(int(j))
    for i in command:
        if i=='R':
            cnt+=1
            #print(cnt)
        elif i=='D':
            #cnt=0
            #print('cnt=',cnt)
            if len(deque)==0:
                print('error')
                error=1
                break
            if cnt%2==0:
                deque.popleft()
            else:
                deque.pop()

    if error==0:
        #print(deque)
        print('[',end='')
        while len(deque)>1:
            if cnt % 2 == 0:
                print(deque.popleft(),end=',')
            else:
                print(deque.pop(),end=',')
        if(len(deque)==1):
            print(deque.pop(),end='')
        print(']')



