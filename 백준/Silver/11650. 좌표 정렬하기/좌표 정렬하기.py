N=int(input())
coordinate=[]
for _ in range(N):
    x,y=map(int, input().split())
    coordinate.append([x,y])

for i in sorted(coordinate):
    print(str(i).replace('[','').replace(']',''
                                         ).replace(',',''))

