import sys

def make_progression(i): #i는 추가할 번호 (1,2,3)
    i+=1 
    if i>3: #1,2,3이 다 안되면 이전 수를 증가시킴 1213121(다음에 1,2,3 다 안됨) ->1213122
        pre_index=progression.pop()
        make_progression(pre_index)
        return

    if len(progression)==N: #종료조건 : 수열의 완성
        print(''.join(map(str,progression)))
        return

    progression.append(i) #우선 수열에 넣는다!
    #나쁜 수열인지 확인
    if len(progression)!=1:
        for k in range(1,len(progression)+1//2):
            #print(progression[-k:], progression[-(2*k):-k])
            if progression[-k:] == progression[-(2*k):-k]:
                progression.pop() #나쁜 수열일때 그자리수를 하나 증가해서 넣기 ex) 1 2 1 2 -> 1 2 1 3
                make_progression(i)
                return

    #현재까지 좋은 수열!
    make_progression(0) #다음 자리수 넣기


N=int(sys.stdin.readline())
nums=[1,2,3]
progression=[]
make_progression(0)

