import sys
n=int(sys.stdin.readline())
tr=[]
for i in range(n):
    tr.append(list(map(int,sys.stdin.readline().strip().split(' '))))
tr.append([0]*n)

for i in range(1,n):
    for j in range(len(tr[i])):
        if j==0:
            #print('1=',i,j)
            tr[i][j]=tr[i-1][j]+tr[i][j]
        elif j==len(tr[i])-1:
            #print('2=',i,j)
            tr[i][j]=tr[i-1][-1]+tr[i][j]
        else:
            #print('3=',i,j)
            tr[i][j]=max(tr[i][j]+tr[i-1][j-1],tr[i][j]+tr[i-1][j])


print(max(tr[n-1]))