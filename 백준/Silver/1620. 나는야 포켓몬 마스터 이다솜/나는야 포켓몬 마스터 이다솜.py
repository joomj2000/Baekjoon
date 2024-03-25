import sys
N, M = map(int, sys.stdin.readline().split())
dic_name={}
dic_number={}

for i in range(N):
    n=sys.stdin.readline().rstrip()
    dic_number[i+1]=n
    dic_name[n]=i+1
for i in range(M):
    m = sys.stdin.readline().rstrip()
    if m.isnumeric(): #정수이면 number이 key로 저장된 dic에서 value반환
        print(dic_number[int(m)])
    else : #정수가 아니면 name이 key로 저장된 dic에서 value반환 
        print(dic_name[m])

