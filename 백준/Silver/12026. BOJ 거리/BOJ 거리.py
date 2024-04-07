import sys

N=int(sys.stdin.readline())
road=sys.stdin.readline()
d=[1000001]*len(road)
d[0]=0
for i in range(1,len(road)):
    if road[i]=='B':
        for j in range(0,i):
            if road[j]=='J':
                d[i]=min(d[i],(i-j)*(i-j)+d[j])
    elif road[i]=='O':
        for j in range(0, i):
            if road[j] == 'B':
                d[i] = min(d[i], (i-j)*(i-j)+d[j])
    else:
        for j in range(0, i):
            if road[j] == 'O':
                d[i] = min(d[i], (i-j)*(i-j)+d[j])
if d[N-1]==1000001:
    print(-1)
else:
    print(d[N-1])