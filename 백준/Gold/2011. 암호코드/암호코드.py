import sys
'''
현재자리수가 0보다 클때 -> 이전 dp값 더하기 마지막에 원소 하나만 플러스됨
현재자리수와 이전 자리수를 합쳤을때 10~26사이의 수일때 -> 전전dp 값 더하기

'''

N=sys.stdin.readline().strip()
d=[0]*(len(N)+1)
if N[0]=='0':
    print(0)
    exit()

d[0]=1
d[1]=1
for i in range(2,len(N)+1):
    if int(N[i-1])>0:
        d[i]+=d[i-1]
    if 26>=int(N[i-2]+N[i-1])>=10:
        d[i]+=d[i-2]
    if int(N[i-1])==0 and int(N[i-2])>2:
        print(0)
        exit()
print((d[len(N)])%1000000)