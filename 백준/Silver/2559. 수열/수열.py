N,K=map(int,input().split())

n_list=list(map(int,input().split()))
#print(n_list)

result=0
for i in range(K):
    result+=n_list[i]

x=0
y=K
max_temp=result
while(y<N):
    result-=n_list[x]
    result+=n_list[y]
    if result>max_temp:
        max_temp=result
    x+=1
    y+=1

print(max_temp)